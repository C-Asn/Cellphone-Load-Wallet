class LoadWallet:
    def __init__(self, owner_name, mobile_number, balance):
        self.owner_name = owner_name
        self.mobile_number = mobile_number
        self.balance = balance

    def top_up(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"New balance: P{self.balance:.2f}")

    def send_load(self, number, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Sent P{amount:.2f} to {number}.")
            print(f"New balance: P{self.balance:.2f}")

    def send_with_fee(self, number, amount):
        # A fixed P5 service fee applies to other networks.
        fee = 5
        total = amount + fee

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif total > self.balance:
            print("Insufficient balance, including the P5.00 service fee.")
        else:
            self.balance -= total
            print(f"Sent P{amount:.2f} to {number}.")
            print(f"Service fee: P{fee:.2f}")
            print(f"New balance: P{self.balance:.2f}")

    def show_balance(self):
        print(f"Owner         : {self.owner_name}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self.balance:.2f}")
