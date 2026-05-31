# List of stock prices
prices = [2450, 3890, 980, 1520, 3400]

print("Stock prices:")
for price in prices:
    print(price)

# Dictionary of stocks and prices
stocks = {
    "RELIANCE": 2450,
    "TCS": 3890,
    "INFY": 1520,
    "HDFCBANK": 1700,
    "ITC": 420
}

print("\nStock data:")

for company, price in stocks.items():
    print(company, ":", price)

    # Function to calculate PE ratio

def calc_pe(price, eps):
    pe = price / eps
    return pe


stock_price = float(input("Enter stock price: "))
eps = float(input("Enter EPS: "))

result = calc_pe(stock_price, eps)

print("PE Ratio =", result)