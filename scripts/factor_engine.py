
# =========================================
# Quant Factor Engine
# =========================================

import yfinance as yf
import pandas as pd
import numpy as np


# =========================================
# Factor Engine
# =========================================

def factor_engine(stock):


    # =========================================
    # Download Data
    # =========================================

    ticker = yf.Ticker(stock)

    data = ticker.history(
        period="2y"
    )


    info = ticker.info


    # =========================================
    # Safety Check
    # =========================================

    if data.empty:

        return None


    # =========================================
    # Returns
    # =========================================

    data["Returns"] = data["Close"].pct_change()


    # =========================================
    # Momentum Factor
    # =========================================

    momentum_6m = (

        (

            data["Close"].iloc[-1]

            /

            data["Close"].iloc[-126]

        )

        - 1

    ) * 100


    # =========================================
    # Volatility Factor
    # =========================================

    volatility = (

        data["Returns"].std()

        *

        np.sqrt(252)

        *

        100

    )


    # =========================================
    # Trend Strength
    # =========================================

    ma50 = data["Close"].rolling(50).mean()

    ma200 = data["Close"].rolling(200).mean()


    latest_price = data["Close"].iloc[-1]


    if latest_price > ma50.iloc[-1] > ma200.iloc[-1]:

        trend = "Strong Uptrend"

    elif latest_price < ma50.iloc[-1] < ma200.iloc[-1]:

        trend = "Strong Downtrend"

    else:

        trend = "Sideways"


    # =========================================
    # Volume Expansion
    # =========================================

    avg_volume = data["Volume"].rolling(20).mean()


    latest_volume = data["Volume"].iloc[-1]


    if latest_volume > avg_volume.iloc[-1]:

        volume_factor = "High Participation"

    else:

        volume_factor = "Low Participation"


    # =========================================
    # Fundamental Factors
    # =========================================

    roe = info.get(
        "returnOnEquity",
        0
    )

    debt_to_equity = info.get(
        "debtToEquity",
        0
    )

    revenue_growth = info.get(
        "revenueGrowth",
        0
    )

    profit_margin = info.get(
        "profitMargins",
        0
    )


    # =========================================
    # Convert percentages
    # =========================================

    if roe:

        roe = roe * 100


    if revenue_growth:

        revenue_growth = revenue_growth * 100


    if profit_margin:

        profit_margin = profit_margin * 100


    # =========================================
    # Return Factors
    # =========================================

    return {

        "momentum_6m": round(
            momentum_6m,
            2
        ),

        "volatility": round(
            volatility,
            2
        ),

        "trend": trend,

        "volume_factor": volume_factor,

        "roe": round(
            roe,
            2
        ) if roe else "N/A",

        "debt_to_equity": round(
            debt_to_equity,
            2
        ) if debt_to_equity else "N/A",

        "revenue_growth": round(
            revenue_growth,
            2
        ) if revenue_growth else "N/A",

        "profit_margin": round(
            profit_margin,
            2
        ) if profit_margin else "N/A"

    }

