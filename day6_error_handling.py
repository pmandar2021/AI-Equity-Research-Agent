def calc_pe(price, eps):
    try:
        pe = price / eps
        return pe
    except ZeroDivisionError:
        return "EPS cannot be zero"


price = float(input("Enter stock price: "))
eps = float(input("Enter EPS: "))

result = calc_pe(price, eps)

print("Result:", result)