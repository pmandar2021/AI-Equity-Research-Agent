# =========================================
# AI Scoring Engine
# =========================================

def scoring_engine(

    tech,
    fund,
    news

):

    score = 50

    # =========================================
    # Technical trend
    # =========================================

    if tech["signal"] == "BUY 📈":

        score += 20

    elif tech["signal"] == "SELL 📉":

        score -= 20


    # =========================================
    # RSI
    # =========================================

    if 40 <= tech["rsi"] <= 65:

        score += 10

    elif tech["rsi"] > 75:

        score -= 10


    # =========================================
    # MACD
    # =========================================

    if "Bullish" in tech["macd"]:

        score += 10

    else:

        score -= 10


    # =========================================
    # Volume
    # =========================================

    if "Increasing" in tech["volume"]:

        score += 5


    # =========================================
    # Fundamentals
    # =========================================

    try:

        pe = float(
            fund["pe"]
        )

        if pe < 25:

            score += 10

        elif pe > 60:

            score -= 10

    except:

        pass


    # =========================================
    # News sentiment
    # =========================================

    try:

        if "Positive" in news["sentiment"]:

            score += 5

        elif "Negative" in news["sentiment"]:

            score -= 5

    except:

        pass


    # =========================================
    # Final cleanup
    # =========================================

    score = max(
        0,
        min(score,100)
    )


    # =========================================
    # Recommendation
    # =========================================

    if score >= 75:

        recommendation = "Strong Buy 🚀"

    elif score >= 60:

        recommendation = "Buy 📈"

    elif score >= 45:

        recommendation = "Hold ⚠️"

    elif score >= 30:

        recommendation = "Sell 📉"

    else:

        recommendation = "Strong Sell 🔻"


    return {

        "ai_score": score,

        "recommendation": recommendation

    }