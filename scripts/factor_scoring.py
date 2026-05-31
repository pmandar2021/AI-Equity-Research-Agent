
# =========================================
# Quant Factor Scoring Model
# =========================================


# =========================================
# Factor Scoring Function
# =========================================

def factor_scoring(factors):


    # =========================================
    # Initialize Score
    # =========================================

    score = 0


    # =========================================
    # Momentum Score
    # =========================================

    if factors["momentum_6m"] > 25:

        score += 20

    elif factors["momentum_6m"] > 10:

        score += 10


    # =========================================
    # Trend Score
    # =========================================

    if factors["trend"] == "Strong Uptrend":

        score += 20

    elif factors["trend"] == "Sideways":

        score += 5


    # =========================================
    # Volume Participation
    # =========================================

    if factors["volume_factor"] == "High Participation":

        score += 10


    # =========================================
    # ROE Score
    # =========================================

    try:

        if factors["roe"] != "N/A":

            if factors["roe"] > 15:

                score += 15

            elif factors["roe"] > 10:

                score += 8

    except:

        pass


    # =========================================
    # Revenue Growth Score
    # =========================================

    try:

        if factors["revenue_growth"] != "N/A":

            if factors["revenue_growth"] > 15:

                score += 15

            elif factors["revenue_growth"] > 8:

                score += 8

    except:

        pass


    # =========================================
    # Debt Score
    # =========================================

    try:

        if factors["debt_to_equity"] != "N/A":

            if factors["debt_to_equity"] < 50:

                score += 10

            elif factors["debt_to_equity"] > 150:

                score -= 10

    except:

        pass


    # =========================================
    # Volatility Penalty
    # =========================================

    if factors["volatility"] > 40:

        score -= 10


    # =========================================
    # Final Classification
    # =========================================

    if score >= 75:

        rating = "Institutional Buy"

    elif score >= 55:

        rating = "Accumulate"

    elif score >= 35:

        rating = "Neutral"

    else:

        rating = "Avoid"


    # =========================================
    # Return Results
    # =========================================

    return {

        "quant_score": score,

        "rating": rating

    }

