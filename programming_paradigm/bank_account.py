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
        """Withdraw a specified amount if funds are sufficient."""
        if amount > self.__account_balance:
            print("Withdraw more than you have.")
            return False
        if amount <=0:
            return False
        self.__account_balance -= amount
        return True
    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
        