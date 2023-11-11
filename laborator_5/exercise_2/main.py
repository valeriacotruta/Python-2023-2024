# Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal, and interest calculation.


import exercise_2 as ex_2

savings_account = ex_2.SavingsAccount(account_number="RO49 AAAA 1B31 0075 9384 0000", current_sum=10)
savings_account.deposit(1000)
savings_account.get_interest(rate=20, years=3)
savings_account.withdrawal(2000)

checking_account = ex_2.CheckingAccount(account_number="RO49 AAAA 1B31 0075 9384 0000", current_sum=500, limit=200)
checking_account.withdrawal(150)
checking_account.withdrawal(700)
