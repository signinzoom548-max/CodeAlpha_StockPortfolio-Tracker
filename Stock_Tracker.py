prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150
}

stock = input("Enter Stock Name (AAPL/TSLA/GOOGLE): ").upper()

quantity = int(input("Enter Quantity: "))

if stock in prices:
    total = prices[stock] * quantity
    print("Total Investment Value =", total)
else:
    print("Stock Not Found")