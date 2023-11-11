class Employee:
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary

    def show_information(self):
        print(f"Name: {self.full_name}, salary: {self.salary}.")
