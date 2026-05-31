import yfinance as yf
import pandas as pd

stock=input("Enter stock symbol: ").strip().upper()

ticker=yf.Ticker(stock)

# Historical data
history=ticker.history(period="1y")

# Company information
info=ticker.info

print("\nCompany Information")
print("-------------------")

print("Company:",info.get("longName","N/A"))
print("Sector:",info.get("sector","N/A"))
print("Industry:",info.get("industry","N/A"))
print("Market Cap:",info.get("marketCap","N/A"))
print("PE Ratio:",info.get("trailingPE","N/A"))

print("\nRecent Data")
print(history.tail())

# Save files
history.to_csv(
    f"data/raw/{stock}_history.csv"
)

print("\nData saved successfully")