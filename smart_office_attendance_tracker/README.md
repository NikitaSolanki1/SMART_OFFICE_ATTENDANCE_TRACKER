# Nikerio Attendance and Salary Tracker

## Description
This is a comprehensive Python project that demonstrates Object-Oriented Programming (OOP) concepts while providing a realistic employee management system. It allows you to manage employees in a company, track various types of attendance, calculate salaries including overtime, and save/load data to/from a file. The system comes pre-loaded with sample employee data for immediate use.

## OOP Concepts Used
- **Class**: Blueprint for creating objects (e.g., Employee, Company).
- **Object**: Instance of a class (e.g., a specific employee).
- **Constructor (__init__)**: Method to initialize objects with comprehensive employee details.
- **Instance Variables**: Variables unique to each object (e.g., name, salary, department, attendance records).
- **Class Variables**: Variables shared by all instances (e.g., company name).
- **Instance Methods**: Methods that operate on an instance (e.g., mark_attendance, calculate_salary).
- **Static Method**: Method that doesn't need an instance (e.g., get_company_policy).
- **Class Method**: Method that operates on the class (e.g., change_company_name).
- **Encapsulation**: Hiding data using private variables (e.g., __secret_code).
- **Inheritance**: One class inherits from another (e.g., Company inherits from Organization).

## How to Run
1. Make sure you have Python installed (version 3.x).
2. Navigate to the project directory.
3. Run the main.py file: `python main.py`
4. Follow the menu options in the command line.

## Features
- **Add Employees**: Create new employee records with detailed information including department, position, and contact details
- **Mark Attendance**: Record full days, half days, or absences for employees
- **Add Overtime**: Track and calculate overtime hours with enhanced pay rates
- **View Employee Details**: Display comprehensive employee information including attendance and salary calculations
- **View All Employees**: List all employees in the system
- **Generate Reports**: Create detailed attendance reports with summary statistics
- **Data Persistence**: Save and load employee data to/from a text file with backward compatibility

## Sample Data
The system comes pre-loaded with 10 sample employees across different departments:
- Engineering (Software Engineers, Developers, Tech Leads)
- Marketing (Marketing Managers)
- HR (HR Specialists)
- Sales (Sales Representatives)
- Finance (Accountants)
- Operations (Operations Managers)
- Design (UX Designers)

## Salary Calculation
- Base salary is calculated based on attendance (full days + half days)
- Overtime pay is calculated at 1.5x the regular hourly rate
- Assumes 30 working days and 8 working hours per day for calculations

This project demonstrates real-world HR system concepts while maintaining beginner-friendly, well-commented code.