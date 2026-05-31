

# =========================================
# Multi-Factor Quant Backtest Engine
# =========================================

import yfinance as yf
import pandas as pd
import numpy as np


# =========================================
# Multi-Factor Backtest
# =========================================

def multi_factor_backtest(stock):


    # =========================================
    # Download Data
    # =========================================

    data = yf.download(

        stock,

        period="7y"

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
    # RSI
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
    # Momentum Factor
    # =========================================

    data["Momentum"] = (

        data["Close"]

        /

        data["Close"].shift(126)

    ) - 1


    # =========================================
    # Volume Factor
    # =========================================

    data["AvgVolume"] = data[
        "Volume"
    ].rolling(20).mean()


    # =========================================
    # Multi-Factor Signal
    # =========================================

    data["Signal"] = 0


    buy_condition = (

        (data["RSI"] < 30)

        &

        (data["MA50"] > data["MA200"])

        &

        (data["Momentum"] > 0)

        &

        (data["Volume"].squeeze() > data["AvgVolume"].squeeze())

    )


    sell_condition = (

        (data["RSI"] > 70)

        |

        (data["MA50"] < data["MA200"])

    )


    data.loc[
        buy_condition,
        "Signal"
    ] = 1


    data.loc[
        sell_condition,
        "Signal"
    ] = 0


    # =========================================
    # Forward Fill Positions
    # =========================================

    data["Position"] = data[
        "Signal"
    ].replace(
        to_replace=0,
        method="ffill"
    )


    data["Position"] = data[
        "Position"
    ].fillna(0)


    # =========================================
    # Strategy Returns
    # =========================================

    data["Strategy_Returns"] = (

        data["Position"]
        .shift(1)

        *

        data["Returns"]

    )


    # =========================================
    # Equity Curves
    # =========================================

    data["Cumulative_Strategy"] = (

        1 + data["Strategy_Returns"]

    ).cumprod()


    data["Cumulative_Market"] = (

        1 + data["Returns"]

    ).cumprod()


    # =========================================
    # Performance Metrics
    # =========================================

    strategy_return = (

        data["Cumulative_Strategy"]
        .iloc[-1]

        - 1

    ) * 100


    benchmark_return = (

        data["Cumulative_Market"]
        .iloc[-1]

        - 1

    ) * 100


    sharpe = (

        data["Strategy_Returns"]
        .mean()

        /

        data["Strategy_Returns"]
        .std()

    ) * np.sqrt(252)


    volatility = (

        data["Strategy_Returns"]
        .std()

        *

        np.sqrt(252)

        *

        100

    )


    # =========================================
    # Drawdown
    # =========================================

    cumulative = data[
        "Cumulative_Strategy"
    ]


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
    # Return Results
    # =========================================

    return {

        "strategy_return": round(
            strategy_return,
            2
        ),

        "benchmark_return": round(
            benchmark_return,
            2
        ),

        "sharpe": round(
            sharpe,
            2
        ),

        "volatility": round(
            volatility,
            2
        ),

        "max_drawdown": round(
            max_drawdown,
            2
        ),

        "data": data

    }

