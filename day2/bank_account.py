class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, account_holder, balance=0):
        if not account_holder.strip():
            raise ValueError("Account holder name cannot be empty.")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        print(f"Deposit successful: Rs. {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        print(f"Withdrawal successful: Rs. {amount:.2f}")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: Rs. {self.balance:.2f}")

    def __str__(self):
        return (
            f"BankAccount(holder={self.account_holder}, "
            f"balance=Rs. {self.balance:.2f})"
        )


def main():
    try:
        name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))

        account = BankAccount(name, initial_balance)

        deposit_amount = float(input("Enter deposit amount: "))
        account.deposit(deposit_amount)

        withdrawal_amount = float(input("Enter withdrawal amount: "))
        account.withdraw(withdrawal_amount)

        print("\nAccount Summary")
        account.display_balance()
        print(account)

    except ValueError as error:
        print("Transaction error:", error)


if __name__ == "__main__":
    main()
