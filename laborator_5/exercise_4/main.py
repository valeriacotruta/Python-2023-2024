# Build an employee hierarchy with a base class Employee.
# Create subclasses for different types of employees like Manager, Engineer, and Salesperson.
# Each subclass should have attributes like salary and methods related to their roles.

import exercise_4 as ex_4

manager = ex_4.Manager(full_name="Kendall Benton", salary=80000, department="Sales")
manager.show_information()

engineer = ex_4.Engineer(full_name="Kieran Holland", salary=90000, department="Sales", programming_language="Python, Java")
engineer.show_information()

salesperson = ex_4.Salesperson(full_name="Astrid Felix", salary=70000, sales_number=150000)
salesperson.show_information()
