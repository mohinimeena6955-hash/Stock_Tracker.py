def stock_tracker():
    # Predefined stock prices
    prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 140,
        "MSFT": 300
    }

    total = 0

    print("Available Stocks:", ", ".join(prices.keys()))

    while True:
        stock = input("Enter stock name (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in prices:
            print("Invalid stock name!")
            continue

        try:
            qty = int(input("Enter quantity: "))
        except:
            print("Enter a valid number!")
            continue

        total += prices[stock] * qty

    print("\n💰 Total Investment Value:", total)

# Run
stock_tracker()
