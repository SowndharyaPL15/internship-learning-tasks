class BankAccount:
    def __init__(self, account_holder, balance=0):
        if not account_holder.strip():
            raise ValueError("Account holder name cannot be empty.")

        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")

        self.balance += amount

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Balance: Rs. {self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, minimum_balance=500):
        super().__init__(account_holder, balance)

        if minimum_balance < 0:
            raise ValueError("Minimum balance cannot be negative.")

        if balance < minimum_balance:
            raise ValueError("Initial balance is below the minimum.")

        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")

        if self.balance - amount < self.minimum_balance:
            raise ValueError("Minimum balance must be maintained.")

        self.balance -= amount

account = SavingsAccount("Sowndharya", 2000)

account.deposit(500)
account.withdraw(300)
account.display_balance()
assert account.balance == 2200
assert account.minimum_balance == 500

print("All assertions passed!")
