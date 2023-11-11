class Account:
    def __init__(self, account_number, current_sum = 0):
        self.account_number = account_number
        self.current_sum = current_sum

    def deposit(self, amount):
        self.current_sum += amount
        print(f"You deposited {amount} lei. Your current sum is: {self.current_sum} lei.")

    def withdrawal(self, amount):
        if self.current_sum < amount:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"You withdrew {amount} lei. Current sum is: ${self.current_sum} lei.")

