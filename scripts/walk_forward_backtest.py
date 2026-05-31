
# =========================================
# Walk Forward Validation Engine
# =========================================

import yfinance as yf
import pandas as pd
import numpy as np


# =========================================
# Walk Forward Test
# =========================================

def walk_forward_test(stock):


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
    # Train/Test Split
    # =========================================

    split = int(

        len(data) * 0.7

    )


    train = data.iloc[:split]

    test = data.iloc[split:]


    # =========================================
    # Optimization on Train Data
    # =========================================

    best_sharpe = -999

    best_rsi = None


    for rsi_level in range(25, 60, 5):


        temp = train.copy()


        temp["Signal"] = 0


        condition = (

            (temp["RSI"] < rsi_level)

            &

            (temp["MA50"] > temp["MA200"])

        )


        temp.loc[
            condition,
            "Signal"
        ] = 1


        temp["Strategy_Returns"] = (

            temp["Signal"]
            .shift(1)

            *

            temp["Returns"]

        )


        sharpe = (

            temp["Strategy_Returns"]
            .mean()

            /

            temp["Strategy_Returns"]
            .std()

        ) * np.sqrt(252)


        if sharpe > best_sharpe:

            best_sharpe = sharpe

            best_rsi = rsi_level


    # =========================================
    # Test on Unseen Data
    # =========================================

    test["Signal"] = 0


    test_condition = (

        (test["RSI"] < best_rsi)

        &

        (test["MA50"] > test["MA200"])

    )


    test.loc[
        test_condition,
        "Signal"
    ] = 1


    test["Strategy_Returns"] = (

        test["Signal"]
        .shift(1)

        *

        test["Returns"]

    )


    # =========================================
    # Performance
    # =========================================

    cumulative = (

        1 + test["Strategy_Returns"]

    ).cumprod()


    total_return = (

        cumulative.iloc[-1]

        - 1

    ) * 100


    sharpe = (

        test["Strategy_Returns"]
        .mean()

        /

        test["Strategy_Returns"]
        .std()

    ) * np.sqrt(252)


    volatility = (

        test["Strategy_Returns"]
        .std()

        *

        np.sqrt(252)

        *

        100

    )


    # =========================================
    # Benchmark
    # =========================================

    benchmark = (

        1 + test["Returns"]

    ).cumprod()


    benchmark_return = (

        benchmark.iloc[-1]

        - 1

    ) * 100


    # =========================================
    # Return Results
    # =========================================

    return {

        "best_rsi": best_rsi,

        "train_sharpe": round(
            best_sharpe,
            2
        ),

        "test_return": round(
            total_return,
            2
        ),

        "test_sharpe": round(
            sharpe,
            2
        ),

        "benchmark_return": round(
            benchmark_return,
            2
        ),

        "volatility": round(
            volatility,
            2
        )

    }

