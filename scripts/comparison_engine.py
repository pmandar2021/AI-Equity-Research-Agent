# =========================================
# Comparison Engine
# =========================================

import pandas as pd

from technical_analysis import technical_analysis
from fundamental_analysis import fundamental_analysis


def compare_stocks(stock_list):

    results=[]


    for stock in stock_list:


        tech=technical_analysis(
            stock
        )
        


        fund=fundamental_analysis(
            stock
        )


        results.append({

            "Stock":stock,

            "Signal":tech["signal"],

            "RSI":round(
                tech["rsi"],
                2
            ),

            "PE":fund["pe"],

            "Business Score":
            fund["score"]

        })


    return pd.DataFrame(
        results
    )