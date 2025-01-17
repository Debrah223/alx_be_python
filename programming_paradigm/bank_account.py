class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account balance, defaulting to zero."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withfraw a specified amount if funds are sufficient."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False
    def display_balance(self):
        """Display the current balance."""
        print(f"Current balance: ${self.__account_balance:.2f}")
        