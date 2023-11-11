from Employee import Employee


class Manager(Employee):
    def __init__(self, full_name, salary, department):
        super().__init__(full_name, salary)
        self.department = department

    def show_information(self):
        print(f"Name: {self.full_name}, department: {self.department}, salary: {self.salary}.")
