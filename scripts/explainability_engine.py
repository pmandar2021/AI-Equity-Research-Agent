# =========================================
# Explainability Engine
#
# Purpose:
# Explain WHY AI generated
# a recommendation
# =========================================


def explainability_engine(
    technical,
    fundamental,
    news
):

    reasons=[]


    # Technical checks

    if "Bullish" in technical["macd"]:

        reasons.append(
            "✓ Bullish MACD momentum"
        )


    if technical["rsi"]>70:

        reasons.append(
            "⚠ RSI indicates overbought condition"
        )


    if "Weak" in technical["volume"]:

        reasons.append(
            "⚠ Weak trading volume"
        )


    # Fundamental checks

    if fundamental["score"]>=80:

        reasons.append(
            "✓ Strong business quality"
        )


    # News checks

    if "Positive" in news["sentiment"]:

        reasons.append(
            "✓ Positive news sentiment"
        )


    return reasons