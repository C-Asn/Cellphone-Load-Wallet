from load_wallet import LoadWallet


owner_name = input("Enter owner name: ")
mobile_number = input("Enter mobile number: ")

# Repeat until the user enters a valid starting balance.
while True:
    try:
        balance = float(input("Enter starting balance: P"))
        if balance < 0:
            print("Starting balance cannot be negative.")
        else:
            break
    except ValueError:
        print("Please enter a number.")

wallet = LoadWallet(owner_name, mobile_number, balance)

while True:
    print("\n----- MENU -----")
    print("1. Top Up Load")
    print("2. Send Load (same network)")
    print("3. Send Load (other network, with fee)")
    print("4. Show Balance")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # Handle nonnumeric amounts without stopping the program.
    try:
        if choice == "1":
            amount = float(input("Enter top-up amount: P"))
            wallet.top_up(amount)
        elif choice == "2":
            number = input("Enter recipient number (same network): ")
            amount = float(input("Enter amount to send: P"))
            wallet.send_load(number, amount)
        elif choice == "3":
            number = input("Enter recipient number (other network): ")
            amount = float(input("Enter amount to send: P"))
            wallet.send_with_fee(number, amount)
        elif choice == "4":
            wallet.show_balance()
        elif choice == "5":
            print("Thank you for using Load Wallet!")
            break
        else:
            print("Invalid option. Choose 1 to 5.")
    except ValueError:
        print("Please enter a number for the amount.")
