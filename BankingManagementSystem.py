
"""A simple banking management system using Python OOP."""


class BankAccount:
    """Represent a general bank account."""

    def __init__(self, account_holder, account_number, initial_balance):
        """Initialize account information."""
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposit successful! Balance: {self.__balance:.2f}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance!")
            return

        self.__balance -= amount
        print(f"Withdrawal successful! Balance: {self.__balance:.2f}")

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

    def display_info(self):
        """Display account information."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance:.2f}")


class SavingsAccount(BankAccount):
    """Represent a savings account."""

    def __init__(self, account_holder, account_number,
                 initial_balance, interest_rate):
        """Initialize a savings account."""
        super().__init__(account_holder, account_number, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Add interest to the savings balance."""
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest added: {interest:.2f}")


class CurrentAccount(BankAccount):
    """Represent a current account with an overdraft facility."""

    def __init__(self, account_holder, account_number,
                 initial_balance, overdraft_limit):
        """Initialize a current account."""
        super().__init__(account_holder, account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Withdraw money within the overdraft limit."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.get_balance() + self.overdraft_limit:
            print("Overdraft limit exceeded!")
            return

        new_balance = self.get_balance() - amount

        # Update the private balance through the parent method.
        if amount <= self.get_balance():
            super().withdraw(amount)
        else:
            self.deposit(-amount) if False else None
            # Use the protected-by-validation balance operation below.
            self._set_balance(new_balance)

        print(f"Remaining balance: {self.get_balance():.2f}")

    def _set_balance(self, amount):
        """Update balance internally for the overdraft operation."""
        self._BankAccount__balance = amount


class Bank:
    """Manage multiple bank accounts."""

    def __init__(self):
        """Initialize the bank."""
        self.accounts = []

    def add_account(self, account):
        """Add a new account."""
        if self.find_account(account.account_number):
            print("Account number already exists!")
            return

        self.accounts.append(account)
        print("Account created successfully!")

    def find_account(self, account_number):
        """Find an account using its account number."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def display_all_accounts(self):
        """Display all registered accounts."""
        if not self.accounts:
            print("No accounts found.")
            return

        for account in self.accounts:
            print("\n--------------------")
            account.display_info()


def main():
    """Run the banking management system."""

    bank = Bank()

    while True:
        print("\n===== ABC BANK =====")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Add Interest")
        print("7. Display All Accounts")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Account holder: ")
                number = input("Account number: ")
                balance = float(input("Initial balance: "))
                rate = float(input("Interest rate (%): "))

                account = SavingsAccount(name, number, balance, rate)
                bank.add_account(account)

            elif choice == 2:
                name = input("Account holder: ")
                number = input("Account number: ")
                balance = float(input("Initial balance: "))
                limit = float(input("Overdraft limit: "))

                account = CurrentAccount(name, number, balance, limit)
                bank.add_account(account)

            elif choice in (3, 4, 5, 6):
                number = input("Account number: ")
                account = bank.find_account(number)

                if account is None:
                    print("Account not found!")
                    continue

                if choice == 3:
                    amount = float(input("Deposit amount: "))
                    account.deposit(amount)

                elif choice == 4:
                    amount = float(input("Withdrawal amount: "))
                    account.withdraw(amount)

                elif choice == 5:
                    print(f"Balance: {account.get_balance():.2f}")

                elif choice == 6:
                    if isinstance(account, SavingsAccount):
                        account.add_interest()
                    else:
                        print("Interest is only available for savings accounts.")

            elif choice == 7:
                bank.display_all_accounts()

            elif choice == 8:
                print("Thank you for using ABC Bank!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()