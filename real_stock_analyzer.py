

#####Price > 20 MA > 50 MA > 200 MA
###### = Strong bullish trend

##### Price < 20 MA < 50 MA < 200 MA
##### = Weak trend

import yfinance as yf
import matplotlib.pyplot as plt

stock = input("Enter stock symbol: ")

data = yf.download(stock, period="6mo")

print("Latest 5 rows:")
print(data.tail())

data["Close"].plot()

plt.title(f"{stock} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")

plt.show()

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stock = input("Enter stock symbol: ")

data = yf.download(stock, period="1y")

close = data["Close"]

# Moving averages
data["MA20"] = close.rolling(20).mean()
data["MA50"] = close.rolling(50).mean()

latest_price = close.iloc[-1]
latest_ma20 = data["MA20"].iloc[-1]
latest_ma50 = data["MA50"].iloc[-1]

print("\nCurrent Analysis")
print("Current Price:", round(float(latest_price),2))
print("20 MA:", round(float(latest_ma20),2))
print("50 MA:", round(float(latest_ma50),2))

# Buy/Sell logic
if latest_price > latest_ma20 > latest_ma50:
    signal = "BUY 📈"

elif latest_price < latest_ma20 < latest_ma50:
    signal = "SELL 📉"

else:
    signal = "HOLD ⚠️"

print("\nSignal:", signal)

# Plot
plt.figure(figsize=(12,6))

plt.plot(close,label="Close Price")
plt.plot(data["MA20"],label="20 MA")
plt.plot(data["MA50"],label="50 MA")

plt.title(f"{stock} Analysis")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid()

plt.show()