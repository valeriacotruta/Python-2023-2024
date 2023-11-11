from exercise_2.Account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, current_sum=0):
        super().__init__(account_number, current_sum)

    def get_interest(self, rate=10, years=1):
        print(f"Interest for {years} years with {rate}% rate: {self.current_sum * (rate / 100) * years}")
