
# =========================================
# NSE Quant Stock Ranking Engine
# =========================================

import pandas as pd

from factor_engine import factor_engine

from factor_scoring import factor_scoring


# =========================================
# Rank Stocks
# =========================================

def rank_stocks():


    # =========================================
    # Load NSE Database
    # =========================================

    stocks_df = pd.read_csv(
        "data/nse_symbols.csv"
    )


    results = []


    # =========================================
    # Loop Through Stocks
    # =========================================

    for _, row in stocks_df.iterrows():


        try:

            symbol = row["SYMBOL"] + ".NS"

            company = row["NAME"]


            # =========================================
            # Generate Factors
            # =========================================

            factors = factor_engine(
                symbol
            )


            if factors is None:

                continue


            # =========================================
            # Generate Score
            # =========================================

            score = factor_scoring(
                factors
            )


            # =========================================
            # Store Results
            # =========================================

            results.append({

                "Company": company,

                "Symbol": symbol,

                "Quant Score": score[
                    "quant_score"
                ],

                "Rating": score[
                    "rating"
                ],

                "Momentum 6M": factors[
                    "momentum_6m"
                ],

                "ROE": factors[
                    "roe"
                ],

                "Revenue Growth": factors[
                    "revenue_growth"
                ],

                "Volatility": factors[
                    "volatility"
                ]

            })


            print(
                f"Processed: {symbol}"
            )


        except Exception as e:

            print(
                f"Error with {symbol}: {e}"
            )


    # =========================================
    # Final DataFrame
    # =========================================

    final_df = pd.DataFrame(
        results
    )


    # =========================================
    # Sort Rankings
    # =========================================

    final_df = final_df.sort_values(

        by="Quant Score",

        ascending=False

    )


    # =========================================
    # Top Stocks
    # =========================================

    return final_df.head(20)

