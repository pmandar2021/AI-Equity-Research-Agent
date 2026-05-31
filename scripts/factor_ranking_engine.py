# =========================================
# Factor Ranking Engine
# =========================================

import pandas as pd

from scripts.factor_engine import factor_engine


def rank_stocks(stock_list):

    results = []

    for stock in stock_list:

        try:

            factors = factor_engine(stock)

            if factors is None:
                continue

            results.append({

                "Symbol": stock,

                "Momentum":
                factors["momentum_6m"],

                "ROE":
                factors["roe"]
                if factors["roe"] != "N/A"
                else 0,

                "Growth":
                factors["revenue_growth"]
                if factors["revenue_growth"] != "N/A"
                else 0,

                "Volatility":
                factors["volatility"]

            })

        except Exception as e:

            print(
                f"Error: {stock} -> {e}"
            )

    df = pd.DataFrame(results)

    # Higher better

    df["Momentum_Rank"] = (
        df["Momentum"]
        .rank(pct=True)
        * 100
    )

    df["ROE_Rank"] = (
        df["ROE"]
        .rank(pct=True)
        * 100
    )

    df["Growth_Rank"] = (
        df["Growth"]
        .rank(pct=True)
        * 100
    )

    # Lower volatility better

    df["Volatility_Rank"] = (
        (
            len(df)
            -
            df["Volatility"]
            .rank()
            +
            1
        )
        /
        len(df)
    ) * 100

    # Composite Score

    df["Total_Score"] = (

        0.30 * df["Momentum_Rank"]

        +

        0.30 * df["ROE_Rank"]

        +

        0.20 * df["Growth_Rank"]

        +

        0.20 * df["Volatility_Rank"]

    )

    df = df.sort_values(

        by="Total_Score",

        ascending=False

    )

    return df