stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total = 0

print("Welcome to the Stock Tracker!")
print("Available stocks:", ", ".join(stock_prices))
print("Type 'done' when you are finished.\n")

while True:
    name = input("Enter stock name: ").upper().strip()

    if name == "DONE":
        break

    if name not in stock_prices:
        print("Sorry, that stock is not in the list.\n")
        continue

    qty_text = input("Enter quantity: ").strip()

    if not qty_text.isdigit() or int(qty_text) <= 0:
        print("Please enter a whole number greater than 0.\n")
        continue

    qty = int(qty_text)

    # add to existing quantity if the stock was already entered
    if name in portfolio:
        portfolio[name] += qty
    else:
        portfolio[name] = qty

    print("Added", qty, "share(s) of", name, "\n")

if len(portfolio) == 0:
    print("No stocks entered.")
else:
    print("\n--- Your Investment ---")
    for name in portfolio:
        qty = portfolio[name]
        value = qty * stock_prices[name]
        total += value
        print(name, "-", qty, "x", stock_prices[name], "=", value)

    print("-----------------------")
    print("Total investment:", total)

    save = input("\nSave result to a file? (y/n): ").lower().strip()

    if save == "y":
        file = open("investment.txt", "w")
        file.write("Stock Investment Summary\n")
        file.write("------------------------\n")
        for name in portfolio:
            qty = portfolio[name]
            value = qty * stock_prices[name]
            file.write(name + " - " + str(qty) + " x " + str(stock_prices[name]) + " = " + str(value) + "\n")
        file.write("------------------------\n")
        file.write("Total investment: " + str(total) + "\n")
        file.close()
        print("Saved to investment.txt")
