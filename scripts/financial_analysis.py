# =========================================
# Financial Analysis Module
# =========================================

import yfinance as yf
import pandas as pd


def financial_analysis(stock):

    ticker = yf.Ticker(stock)


    # Income statement
    financials = ticker.financials


    if financials.empty:

        return None


    # Revenue row
    revenue = financials.loc["Total Revenue"]


    # Net Income row
    income = financials.loc["Net Income"]


    data = pd.DataFrame({

        "Year": revenue.index.astype(str),

        "Revenue": revenue.values,

        "NetIncome": income.values

    })


    return data