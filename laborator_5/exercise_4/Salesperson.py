from Employee import Employee


class Salesperson(Employee):
    def __init__(self, full_name, salary, sales_number):
        super().__init__(full_name, salary)
        self.sales_number = sales_number

    def show_information(self):
        print(f"Name: {self.full_name}, salary: {self.salary}."
              f"Sales number: {self.sales_number}.")
