# =========================================
# News + Sentiment Engine
#
# Purpose:
# Get latest company news and estimate
# sentiment score
# =========================================

import yfinance as yf


# =========================================
# Main Function
# =========================================

def news_analysis(stock):

    # Create stock object
    ticker = yf.Ticker(stock)

    # Fetch news
    news = ticker.news


    # =========================================
    # Safety check
    # =========================================

    if not news:

        return {

            "headline":"No news available",

            "sentiment":"Neutral 😐"

        }


    # =========================================
    # Extract headline safely
    # =========================================

    try:

        # New Yahoo structure
        latest_headline = news[0]["content"]["title"]

    except:

        try:

            # Old structure
            latest_headline = news[0]["title"]

        except:

            latest_headline = "Headline unavailable"


    # =========================================
    # Sentiment Keywords
    # =========================================

    positive_words = [

        "growth",
        "profit",
        "record",
        "approval",
        "expansion",
        "gain",
        "order",
        "surge"
    ]


    negative_words = [

        "loss",
        "decline",
        "fraud",
        "drop",
        "fall",
        "lawsuit",
        "risk"
    ]


    score = 0

    headline_lower = latest_headline.lower()


    # Positive score

    for word in positive_words:

        if word in headline_lower:

            score += 1


    # Negative score

    for word in negative_words:

        if word in headline_lower:

            score -= 1


    # =========================================
    # Final sentiment
    # =========================================

    if score > 0:

        sentiment = "Positive 📈"

    elif score < 0:

        sentiment = "Negative 📉"

    else:

        sentiment = "Neutral 😐"


    # Return results

    return {

        "headline": latest_headline,

        "sentiment": sentiment
    }