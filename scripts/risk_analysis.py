# =========================================
# Risk Analysis Module
# =========================================

import yfinance as yf
import pandas as pd
import numpy as np


def risk_analysis(stock):


    # Download stock data

    data = yf.download(

        stock,

        period="1y"

    )


    # Daily returns

    data["Returns"] = (

        data["Close"]

        .pct_change()

    )


    # Annual volatility

    volatility = (

        data["Returns"]

        .std()

        * np.sqrt(252)

        *100
    )


    # Sharpe Ratio

    sharpe = (

        data["Returns"]

        .mean()

        /

        data["Returns"]

        .std()

    )*np.sqrt(252)


    # Maximum Drawdown

    cumulative = (

        1 +

        data["Returns"]

    ).cumprod()


    peak = cumulative.cummax()


    drawdown = (

        (cumulative-peak)

        /peak

    )


    max_drawdown = (

        drawdown.min()

        *100
    )


    return {

        "volatility":

        round(
            volatility,
            2
        ),

        "sharpe":

        round(
            sharpe,
            2
        ),

        "max_drawdown":

        round(
            max_drawdown,
            2
        )

    }