# ============================================================
# CODEALPHA PYTHON INTERNSHIP
# TASK 2: STOCK PORTFOLIO TRACKER
# ============================================================

# Hardcoded dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

print("=" * 50)
print("          STOCK PORTFOLIO TRACKER")
print("=" * 50)

# Display available stocks
print("\nAvailable Stocks and Prices:")
print("-" * 35)

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("-" * 35)

# Take input from user
number_of_stocks = int(input("\nHow many different stocks do you want to add? "))

# Dictionary to store user's portfolio
portfolio = {}

# Calculate investment for each stock
for i in range(number_of_stocks):

    print(f"\n--- Stock {i + 1} ---")

    stock_name = input("Enter stock name: ").upper()

    # Check if stock is available
    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]
        investment = price * quantity

        # Store stock information
        portfolio[stock_name] = {
            "quantity": quantity,
            "price": price,
            "investment": investment
        }

    else:
        print("❌ Stock not available.")
        print("Please choose from:", ", ".join(stock_prices.keys()))

# Calculate total investment
total_investment = 0

print("\n" + "=" * 60)
print("                  PORTFOLIO SUMMARY")
print("=" * 60)

if len(portfolio) > 0:

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment':<15}")
    print("-" * 60)

    for stock, details in portfolio.items():

        print(
            f"{stock:<10}"
            f"{details['quantity']:<12}"
            f"${details['price']:<11}"
            f"${details['investment']:<15}"
        )

        total_investment += details["investment"]

    print("-" * 60)
    print(f"TOTAL INVESTMENT: ${total_investment:.2f}")
    print("=" * 60)

    # Save the result in a TXT file
    with open("stock_portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=" * 50 + "\n\n")

        for stock, details in portfolio.items():

            file.write(f"Stock: {stock}\n")
            file.write(f"Quantity: {details['quantity']}\n")
            file.write(f"Price: ${details['price']}\n")
            file.write(f"Investment: ${details['investment']}\n")
            file.write("-" * 30 + "\n")

        file.write(f"\nTOTAL INVESTMENT: ${total_investment:.2f}\n")

    print("\n✅ Portfolio saved successfully!")
    print("📁 File created: stock_portfolio.txt")

else:
    print("No stocks were added to the portfolio.")