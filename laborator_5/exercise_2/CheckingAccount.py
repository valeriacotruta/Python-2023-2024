from exercise_2.Account import Account


class CheckingAccount(Account):

    def __init__(self, account_number, current_sum=0, limit=100):
        super().__init__(account_number, current_sum)
        self.limit = limit

    def withdrawal(self, amount):
        if self.current_sum + self.limit < amount:
            print("Insufficient funds!")
        else:
            self.current_sum -= amount
            print(f"You withdrew {amount} lei. Current sum: {self.current_sum} lei.")
