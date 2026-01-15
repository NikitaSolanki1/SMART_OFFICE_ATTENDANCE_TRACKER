# employee.py
# This file contains the Employee class, which represents an employee in the company.
# It uses Object-Oriented Programming concepts like class, object, constructor, instance variables, class variables, instance methods, static method, and encapsulation.

from datetime import datetime

class Employee:
    # Class variable: shared by all instances of the class
    # This represents the company name, same for all employees
    company = "Nikerio"

    def __init__(self, employee_id, name, monthly_salary, department="General", position="Employee", email=None, hire_date=None):
        # Constructor: initializes the object when created
        # Instance variables: unique to each object
        self.employee_id = employee_id  # Unique ID for the employee
        self.name = name  # Name of the employee
        self.monthly_salary = monthly_salary  # Monthly salary amount
        self.department = department  # Department the employee works in
        self.position = position  # Job position/title
        self.email = email if email else f"{name.lower().replace(' ', '.')}@{self.company.lower().replace(' ', '')}.com"  # Email address
        self.hire_date = hire_date if hire_date else datetime.now().strftime("%Y-%m-%d")  # Date of hire
        self.days_present = 0  # Number of days present, starts at 0
        self.days_absent = 0  # Number of days absent
        self.half_days = 0  # Number of half days worked
        self.overtime_hours = 0  # Overtime hours worked

        # Private variable: starts with __, not accessible directly from outside
        # This is used to store a secret code, private for security reasons
        self.__secret_code = "private123"  # Private variable for demonstration

    def mark_attendance(self, attendance_type="full"):
        # Instance method: marks attendance based on type
        # attendance_type: "full", "half", or "absent"
        if attendance_type == "full":
            self.days_present += 1
            print(f"Full day attendance marked for {self.name}. Days present: {self.days_present}")
        elif attendance_type == "half":
            self.half_days += 1
            print(f"Half day attendance marked for {self.name}. Half days: {self.half_days}")
        elif attendance_type == "absent":
            self.days_absent += 1
            print(f"Absent marked for {self.name}. Days absent: {self.days_absent}")
        else:
            print("Invalid attendance type. Use 'full', 'half', or 'absent'.")

    def add_overtime(self, hours):
        # Instance method: adds overtime hours
        self.overtime_hours += hours
        print(f"Overtime added for {self.name}: {hours} hours. Total overtime: {self.overtime_hours}")

    def calculate_salary(self):
        # Instance method: calculates salary based on attendance and overtime
        # Assumes 30 days in a month for simplicity
        # Half day counts as 0.5 days
        total_working_days = self.days_present + (self.half_days * 0.5)
        daily_salary = self.monthly_salary / 30
        base_salary = daily_salary * total_working_days
        
        # Overtime pay: assume 1.5x rate for overtime hours
        overtime_pay = (self.monthly_salary / 30 / 8) * 1.5 * self.overtime_hours  # Assuming 8 hours per day
        
        earned_salary = base_salary + overtime_pay
        return earned_salary

    def show_details(self):
        # Instance method: displays employee details
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Hire Date: {self.hire_date}")
        print(f"Monthly Salary: ${self.monthly_salary:.2f}")
        print(f"Days Present: {self.days_present}")
        print(f"Half Days: {self.half_days}")
        print(f"Days Absent: {self.days_absent}")
        print(f"Overtime Hours: {self.overtime_hours}")
        print(f"Company: {self.company}")
        # Note: We don't show the private variable here

    @staticmethod
    def get_company_policy():
        # Static method: doesn't need an instance, can be called on the class
        # Returns a general company policy
        return "Attendance is mandatory for salary calculation."

    @classmethod
    def change_company_name(cls, new_name):
        # Class method: operates on the class, can change class variables
        cls.company = new_name
        print(f"Company name changed to {new_name}")