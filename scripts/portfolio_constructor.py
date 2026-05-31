# =========================================
# Portfolio Constructor
# =========================================

import pandas as pd


def build_portfolio(
    ranking_df,
    top_n=5
):

    # =========================================
    # Select Top Stocks
    # =========================================

    portfolio = ranking_df.head(
        top_n
    ).copy()

    # =========================================
    # Equal Weighting
    # =========================================

    portfolio["Weight"] = (
        100 / top_n
    )

    # =========================================
    # Portfolio Output
    # =========================================

    return portfolio[
        [
            "Symbol",
            "Total_Score",
            "Weight"
        ]
    ]