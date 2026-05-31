# =========================================
# Fundamental Analysis Module
#
# Purpose:
# Analyze the business quality of a stock
#
# Input:
# Stock symbol (Example: TRITURBINE.NS)
#
# Output:
# Dictionary containing:
# - Score
# - Verdict
# - Important metrics
# =========================================


# Import library for stock data
import yfinance as yf


# =========================================
# Main Function
# =========================================

def fundamental_analysis(stock):

    # =========================================
    # Create stock object
    # =========================================

    ticker = yf.Ticker(stock)

    # Get company information
    info = ticker.info


    # =========================================
    # Extract financial metrics
    # =========================================

    # Price to Earnings Ratio
    pe = info.get("trailingPE", "N/A")

    # Price to Book Ratio
    pb = info.get("priceToBook", "N/A")

    # Market capitalization
    market_cap = info.get(
        "marketCap",
        None
    )

    # Profit margin
    profit_margin = info.get(
        "profitMargins",
        "N/A"
    )

    # Return on Equity
    roe = info.get(
        "returnOnEquity",
        "N/A"
    )

    # Debt to Equity ratio
    debt_equity = info.get(
        "debtToEquity",
        "N/A"
    )


    # =========================================
    # Convert Market Cap into Crores
    # =========================================

    if market_cap:

        market_cap = round(
            market_cap / 10000000,
            2
        )

        market_cap = f"₹ {market_cap:,} Cr"

    else:

        market_cap = "N/A"


    # =========================================
    # Create Fundamental Score
    # =========================================

    score = 0


    # ROE scoring
    # Good companies generally have ROE >15%

    if roe != "N/A":

        roe_percent = roe * 100

        if roe_percent > 15:

            score += 30


    # Debt scoring
    # Lower debt usually means safer business

    if debt_equity != "N/A":

        if debt_equity < 100:

            score += 25


    # Profit margin scoring
    # Higher margin means stronger business

    if profit_margin != "N/A":

        margin_percent = profit_margin * 100

        if margin_percent > 10:

            score += 25


    # PE scoring
    # Lower PE sometimes indicates better valuation

    if pe != "N/A":

        if pe < 40:

            score += 20


    # =========================================
    # Final Business Verdict
    # =========================================

    if score >= 80:

        verdict = "Strong Business 💪"

    elif score >= 60:

        verdict = "Average Business 👍"

    else:

        verdict = "Weak Fundamentals ⚠️"


    # =========================================
    # Return results to main_agent.py
    # =========================================

    return {

        "score": score,

        "verdict": verdict,

        "market_cap": market_cap,

        "pe": pe,

        "pb": pb,

        "roe": roe,

        "profit_margin": profit_margin,

        "debt_equity": debt_equity
    }