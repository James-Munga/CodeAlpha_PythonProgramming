
# Stock Portfolio Tracker

# Dictionary containing stock names and prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 175
}

# Dictionary to store user stock quantities
portfolio = {}

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Ask user how many different stocks they want
try:
    number_of_stocks = int(input("\nHow many stocks do you want to track? "))

    if number_of_stocks <= 0:
        print("Please enter a number greater than zero.")

    else:

        # Collect stock names and quantities
        for i in range(number_of_stocks):

            stock_name = input("\nEnter stock symbol: ").upper().strip()

            if stock_name not in stock_prices:
                print("Stock not available. Please try again.")
                continue

            try:
                quantity = int(input("Enter quantity owned: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                portfolio[stock_name] = (
                    portfolio.get(stock_name, 0) + quantity
                )

            except ValueError:
                print("Please enter a valid whole number.")

        # Calculate total investment
        total_investment = 0

        print("\n====================================")
        print("          PORTFOLIO SUMMARY")
        print("====================================")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            total_investment += investment

            print("\nStock:", stock)
            print("Price per share: $", price)
            print("Quantity:", quantity)
            print("Investment value: $", investment)

        print("\n------------------------------------")
        print("TOTAL INVESTMENT: $", total_investment)
        print("------------------------------------")

except ValueError:
    print("Please enter a valid number.")
