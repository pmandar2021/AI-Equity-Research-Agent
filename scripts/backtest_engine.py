
# =========================================
# Quant Backtesting Engine
# =========================================

import yfinance as yf
import pandas as pd
import numpy as np


# =========================================
# Backtest Strategy
# =========================================

def backtest_strategy(stock):


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
    # Daily Returns
    # =========================================

    data["Returns"] = data["Close"].pct_change()


    # =========================================
    # Indicators
    # =========================================

    data["MA50"] = data["Close"].rolling(50).mean()

    data["MA200"] = data["Close"].rolling(200).mean()


    # RSI

    delta = data["Close"].diff()

    gain = delta.where(
        delta > 0,
        0
    )

    loss = -delta.where(
        delta < 0,
        0
    )

    avg_gain = gain.rolling(14).mean()

    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    data["RSI"] = 100 - (

        100 / (1 + rs)

    )


    # =========================================
    # Strategy Rules
    # =========================================

    data["Signal"] = 0


    # Buy Condition

    buy_condition = (

        (data["RSI"] < 35)

        &

        (data["MA50"] > data["MA200"])

    )


    data.loc[
        buy_condition,
        "Signal"
    ] = 1


    # =========================================
    # Strategy Returns
    # =========================================

    data["Strategy_Returns"] = (

        data["Signal"]
        .shift(1)

        *

        data["Returns"]

    )


    # =========================================
    # Cumulative Returns
    # =========================================

    data["Cumulative_Market"] = (

        1 + data["Returns"]

    ).cumprod()


    data["Cumulative_Strategy"] = (

        1 + data["Strategy_Returns"]

    ).cumprod()


    # =========================================
    # Performance Metrics
    # =========================================

    total_return = (

        data["Cumulative_Strategy"]
        .iloc[-1]

        - 1

    ) * 100


    benchmark_return = (

        data["Cumulative_Market"]
        .iloc[-1]

        - 1

    ) * 100


    volatility = (

        data["Strategy_Returns"]
        .std()

        *

        np.sqrt(252)

        *

        100

    )


    sharpe = (

        data["Strategy_Returns"]
        .mean()

        /

        data["Strategy_Returns"]
        .std()

    ) * np.sqrt(252)


    # =========================================
    # Drawdown
    # =========================================

    cumulative = data["Cumulative_Strategy"]

    running_max = cumulative.cummax()

    drawdown = (

        cumulative
        -
        running_max

    ) / running_max


    max_drawdown = (

        drawdown.min()

        * 100

    )


    # =========================================
    # Win Rate
    # =========================================

    winning_days = (

        data["Strategy_Returns"] > 0

    ).sum()


    total_days = (

        data["Strategy_Returns"] != 0

    ).sum()


    if total_days > 0:

        win_rate = (

            winning_days
            /
            total_days

        ) * 100

    else:

        win_rate = 0


    # =========================================
    # Return Results
    # =========================================

    return {

        "strategy_return": round(
            total_return,
            2
        ),

        "benchmark_return": round(
            benchmark_return,
            2
        ),

        "volatility": round(
            volatility,
            2
        ),

        "sharpe": round(
            sharpe,
            2
        ),

        "max_drawdown": round(
            max_drawdown,
            2
        ),

        "win_rate": round(
            win_rate,
            2
        ),

        "data": data

    }

