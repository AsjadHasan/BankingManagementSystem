# BankingManagementSystem
Banks use similar systems to manage customer accounts, deposits, withdrawals, and transactions.
<br>
Requirements
<br>
Create the following classes:
<br>

1. BankAccount
- Constructor takes account_holder, account_number, and initial_balance.
- Store account information as instance attributes.
- Use encapsulation for the account balance (__balance).
- Create a deposit(amount) method.
- Create a withdraw(amount) method.
- Create a get_balance() method.
- Prevent withdrawals if the balance is insufficient.
- Prevent negative deposits and withdrawals.
2. SavingsAccount (inherits BankAccount)
- Add an attribute called interest_rate.
- Create a method add_interest() to calculate and add interest to the balance.
3. CurrentAccount (inherits BankAccount)
- Add an attribute called overdraft_limit.
- Allow customers to withdraw beyond their balance, within the overdraft limit.
4. Bank
- Store multiple customer accounts in a list.
- Create an add_account() method.
- Create a find_account() method.
- Create a display_all_accounts() method.