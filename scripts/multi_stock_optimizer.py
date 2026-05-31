
# =========================================
# Multi-Stock Strategy Optimization
# =========================================

import pandas as pd

from scripts.strategy_optimizer import optimize_strategy


# =========================================
# Multi Stock Optimizer
# =========================================

def multi_stock_optimizer():


    # =========================================
    # Test Universe
    # =========================================

    stocks = [

        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ICICIBANK.NS",
        "ITC.NS",
        "BEL.NS",
        "TATAMOTORS.NS"

    ]


    results = []


    # =========================================
    # Loop Through Stocks
    # =========================================

    for stock in stocks:


        try:

            optimization = optimize_strategy(
                stock
            )


            best = optimization.iloc[0]


            results.append({

                "Stock": stock,

                "Best_RSI": best[
                    "RSI_Level"
                ],

                "Best_Sharpe": best[
                    "Sharpe"
                ],

                "Best_Return": best[
                    "Return"
                ]

            })


            print(
                f"Completed: {stock}"
            )


        except Exception as e:

            print(
                f"Error with {stock}: {e}"
            )


    # =========================================
    # Final DataFrame
    # =========================================

    final_df = pd.DataFrame(
        results
    )


    # =========================================
    # Sort by Sharpe
    # =========================================

    final_df = final_df.sort_values(

        by="Best_Sharpe",

        ascending=False

    )


    return final_df

