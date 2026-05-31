# =========================================
# Technical Analysis Module
# =========================================

# Import libraries
import yfinance as yf
import pandas as pd


# =========================================
# Main Function
# =========================================

def technical_analysis(stock):

    # Download stock data
    ticker = yf.Ticker(stock)

    data = ticker.history(
        period="1y"
    )

    # Safety check
    if data.empty:

        print("No stock data found")

        return None


    # =========================================
    # Moving averages
    # =========================================

    data["MA20"] = data["Close"].rolling(
        20
    ).mean()

    data["MA50"] = data["Close"].rolling(
        50
    ).mean()


    # =========================================
    # RSI
    # =========================================

    delta = data["Close"].diff()

    gain = delta.where(
        delta > 0,
        0
    )

    loss = -delta.where(
        delta < 0,
        0
    )

    avg_gain = gain.rolling(
        14
    ).mean()

    avg_loss = loss.rolling(
        14
    ).mean()

    rs = avg_gain / avg_loss

    data["RSI"] = 100 - (
        100 / (1 + rs)
    )


    # =========================================
    # MACD
    # =========================================

    ema12 = data["Close"].ewm(
        span=12
    ).mean()

    ema26 = data["Close"].ewm(
        span=26
    ).mean()

    data["MACD"] = ema12 - ema26

    data["Signal_Line"] = data["MACD"].ewm(
        span=9
    ).mean()


    latest_macd = data["MACD"].iloc[-1]

    latest_signal = data["Signal_Line"].iloc[-1]

    if latest_macd > latest_signal:

        macd_signal = "Bullish 📈"

    else:

        macd_signal = "Bearish 📉"


    # =========================================
    # Support / Resistance
    # =========================================

    latest_support = round(
        data["Low"].tail(20).min(),
        2
    )

    latest_resistance = round(
        data["High"].tail(20).max(),
        2
    )


    # =========================================
    # Volume analysis
    # =========================================

    volume_avg = data["Volume"].rolling(
        20
    ).mean()

    latest_volume = data["Volume"].iloc[-1]

    latest_avg_volume = volume_avg.iloc[-1]

    if latest_volume > latest_avg_volume:

        volume_signal = "Increasing 📈"

    else:

        volume_signal = "Weak 📉"


    # =========================================
    # Latest values
    # =========================================

    price = round(
        float(data["Close"].iloc[-1]),
        2
    )

    ma20 = round(
        float(data["MA20"].iloc[-1]),
        2
    )

    ma50 = round(
        float(data["MA50"].iloc[-1]),
        2
    )

    rsi = round(
        float(data["RSI"].iloc[-1]),
        2
    )


    # =========================================
    # Trading signal
    # =========================================

    if price > ma20 > ma50 and rsi < 70:

        signal = "BUY 📈"

    elif price < ma20 < ma50:

        signal = "SELL 📉"

    else:

        signal = "HOLD ⚠️"


    # =========================================
    # Confidence score
    # =========================================

    score = 0

    if price > ma20 > ma50:
        score += 30

    if 40 <= rsi <= 70:
        score += 20

    if latest_volume > latest_avg_volume:
        score += 20

    if latest_macd > latest_signal:
        score += 30

    confidence = score


    # =========================================
    # Return values
    # =========================================

    return {

        "price": price,
        "signal": signal,
        "rsi": rsi,
        "macd": macd_signal,
        "volume": volume_signal,
        "confidence": confidence,
        "support": latest_support,
        "resistance": latest_resistance,
        "data": data

    }