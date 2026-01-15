# company.py
# This file contains the Company class, which manages a list of employees.
# It demonstrates inheritance by inheriting from a base class (though simple).

# Base class for demonstration of inheritance
class Organization:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Company(Organization):  # Inheritance: Company inherits from Organization
    def __init__(self, name):
        super().__init__(name)  # Call parent constructor
        self.employees = []  # List to store employee objects

    def add_employee(self, employee):
        # Instance method: adds an employee to the list
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.name}")

    def list_employees(self):
        # Instance method: lists all employees
        if not self.employees:
            print("No employees in the company.")
        else:
            print(f"Employees in {self.name}:")
            for emp in self.employees:
                print(f"- {emp.name} (ID: {emp.employee_id})")

    @classmethod
    def show_company_details(cls):
        # Class method: shows general company details
        print("Company Details:")
        print("- This is a .")
        print("- Manages employees, attendance, and salary.")