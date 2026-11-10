# Cellphone Load Wallet

A simple Python OOP activity for managing prepaid load.

## Run the program

Keep both Python files in the same folder and run:

```text
python main.py
```

Enter your answers in the terminal. Enter amounts as numbers, such as `100`.
No additional libraries are needed.

## How the program follows the instructions

- `load_wallet.py` defines the `LoadWallet` class with three attributes: owner name, mobile number, and balance.
- `main.py` imports the class and creates a wallet object using information entered by the user.
- `top_up()` adds load to the balance.
- `send_load()` sends load to the same network by deducting the amount.
- `send_with_fee()` deducts the amount plus a fixed P5 service fee for another network. The fee is an assumption because the instructions do not specify one.
- `show_balance()` displays the owner, mobile number, and current balance.
- A repeating menu uses `input()` and `print()` and stops when the user chooses Exit.
- Basic checks reject negative starting balances, nonpositive transaction amounts, insufficient funds, and ordinary nonnumeric amount input.
- The class groups wallet data and actions together, demonstrating basic encapsulation. The class and main menu are in separate files, as required.

The user selects the network option. Transfers are simulated; the program does not connect to a mobile service.

For example, P100 plus a P50 top-up becomes P150. Sending P20 to the same network leaves P130. Sending another P20 to a different network leaves P105 after the P5 fee.
