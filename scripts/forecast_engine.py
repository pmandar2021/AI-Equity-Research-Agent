# =========================================
# Forecast Engine
# =========================================

import warnings

warnings.filterwarnings("ignore")

import yfinance as yf
import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA


# =========================================
# Forecast Function
# =========================================

def forecast_stock(stock):


    # =========================================
    # Download stock data
    # =========================================

    data = yf.download(

        stock,

        period="1y"

    )


    # =========================================
    # Safety check
    # =========================================

    if data.empty:

        return {

            "trend":"N/A",

            "bull_prob":0,

            "bear_prob":0,

            "lower":"N/A",

            "upper":"N/A",

            "forecast":[]

        }


    # =========================================
    # Prepare close prices
    # =========================================

    close = data["Close"]


    # Add business-day frequency

    close = close.asfreq("B")


    # Fill missing values

    close = close.fillna(
        method="ffill"
    )


    # =========================================
    # ARIMA Model
    # =========================================

    model = ARIMA(

        close,

        order=(2,1,2)

    )


    model_fit = model.fit()


    # =========================================
    # Forecast next 30 business days
    # =========================================

    forecast = model_fit.forecast(
        steps=30
    )


    # =========================================
    # Current price
    # =========================================

    current_price = float(
        close.iloc[-1]
    )


    # =========================================
    # Forecasted future price
    # =========================================

    future_price = float(
        forecast.iloc[-1]
    )


    # =========================================
    # Percentage change
    # =========================================

    change = (

        (

            future_price
            -
            current_price

        )

        /

        current_price

    ) * 100


    # =========================================
    # Trend logic
    # =========================================

    if change > 5:

        trend = "Bullish 📈"

        bull_prob = 70

        bear_prob = 30


    elif change < -5:

        trend = "Bearish 📉"

        bull_prob = 30

        bear_prob = 70


    else:

        trend = "Sideways ↔️"

        bull_prob = 50

        bear_prob = 50


    # =========================================
    # Confidence range
    # =========================================

    std = np.std(
        forecast
    )


    lower = round(

        future_price - std,

        2

    )


    upper = round(

        future_price + std,

        2

    )


    # =========================================
    # Return output
    # =========================================

    return {

        "trend": trend,

        "bull_prob": bull_prob,

        "bear_prob": bear_prob,

        "lower": lower,

        "upper": upper,

        "forecast": forecast

    }