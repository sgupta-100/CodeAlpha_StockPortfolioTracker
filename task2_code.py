# 1. Define stock prices in a dictionary
stock_prices = {"AAPL": 180, "TSLA": 250, "AMZN": 300, "JASPO": 440, "GAME":310}

def main():
    total_investment = 0

    # 2. Taking user inputs for stocks and quantities
    while True:
        stock_name = input("Enter the stock name(or 'quit' to end the count of profit): ").upper()
        if stock_name == 'QUIT':
            break
       
        if stock_name in stock_prices:
            quantity = int(input(f"Enter the quantity for {stock_name}: "))

            # 3. Calculate investment for this stock
            investment = stock_prices[stock_name] * quantity
            total_investment += investment
            print(f"Investment for {stock_name}: ${investment}")
       
        else:
            print("Stock not found. Please enter a valid stock ticker.")

    # 4. Display total investment
    print(f"\nTotal Investment Value: ${total_investment}")

    # 5. Save to file (Optional)
    save_option = input("Do you want to save this result to a file? (yes/no): ").lower()
    if save_option == 'yes':
        file_name = input("Enter the file name (with .txt or .csv): ")
        with open(file_name, 'w') as file:
            file.write(f"Total Investment Value: ${total_investment}\n")
            print(f"Result saved to {file_name}")
   
    else:
        print("File not saved!!")

if __name__ == "__main__":
    main()
