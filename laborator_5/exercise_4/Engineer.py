from Employee import Employee


class Engineer(Employee):
    def __init__(self, full_name, salary, department, programming_language):
        super().__init__(full_name, salary)
        self.department = department
        self.programming_language = programming_language

    def show_information(self):
        print(f"Name: {self.full_name}, department: {self.department}, salary: {self.salary}."
              f"Is coding in {self.programming_language}.")
