# =========================================
# Strategy Optimization Engine
# =========================================

import yfinance as yf
import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA


# =========================================
# Optimize RSI Thresholds
# =========================================

def optimize_strategy(stock):


    # =========================================
    # Download Data
    # =========================================

    data = yf.download(

        stock,

        period="5y"

    )


    # =========================================
    # Safety Check
    # =========================================

    if data.empty:

        return None


    # =========================================
    # Returns
    # =========================================

    data["Returns"] = data[
        "Close"
    ].pct_change()


    # =========================================
    # Moving Averages
    # =========================================

    data["MA50"] = data[
        "Close"
    ].rolling(50).mean()


    data["MA200"] = data[
        "Close"
    ].rolling(200).mean()


    # =========================================
    # RSI Calculation
    # =========================================

    delta = data["Close"].diff()


    gain = delta.where(
        delta > 0,
        0
    )


    loss = -delta.where(
        delta < 0,
        0
    )


    avg_gain = gain.rolling(
        14
    ).mean()


    avg_loss = loss.rolling(
        14
    ).mean()


    rs = avg_gain / avg_loss


    data["RSI"] = 100 - (

        100 / (1 + rs)

    )


    # =========================================
    # Optimization Results
    # =========================================

    results = []


    # =========================================
    # Test Different RSI Levels
    # =========================================

    for rsi_level in range(25, 60, 5):


        temp = data.copy()


        # =========================================
        # Strategy Rules
        # =========================================

        temp["Signal"] = 0


        buy_condition = (

            (temp["RSI"] < rsi_level)

            &

            (temp["MA50"] > temp["MA200"])

        )


        temp.loc[
            buy_condition,
            "Signal"
        ] = 1


        # =========================================
        # Strategy Returns
        # =========================================

        temp["Strategy_Returns"] = (

            temp["Signal"]
            .shift(1)

            *

            temp["Returns"]

        )


        # =========================================
        # Sharpe Ratio
        # =========================================

        sharpe = (

            temp["Strategy_Returns"]
            .mean()

            /

            temp["Strategy_Returns"]
            .std()

        ) * np.sqrt(252)


        # =========================================
        # Total Return
        # =========================================

        cumulative = (

            1 + temp["Strategy_Returns"]

        ).cumprod()


        total_return = (

            cumulative.iloc[-1]

            - 1

        ) * 100


        # =========================================
        # Store Results
        # =========================================

        results.append({

            "RSI_Level": rsi_level,

            "Sharpe": round(
                sharpe,
                2
            ),

            "Return": round(
                total_return,
                2
            )

        })


    # =========================================
    # Final DataFrame
    # =========================================

    results_df = pd.DataFrame(
        results
    )


    # =========================================
    # Sort Best Strategy
    # =========================================

    results_df = results_df.sort_values(

        by="Sharpe",

        ascending=False

    )


    return results_df