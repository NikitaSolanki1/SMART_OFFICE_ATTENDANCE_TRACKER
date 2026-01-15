# file_handler.py
# This file handles saving and loading employee data to/from a text file.
# It demonstrates file handling in Python.

from employee import Employee  # Import at the top to avoid issues

def save_employees_to_file(employees, filename="employees.txt"):
    # Function to save employee data to a file
    # employees: list of Employee objects
    # filename: name of the file to save to
    try:
        with open(filename, 'w') as file:  # Open file in write mode
            for emp in employees:
                # Write each employee's data as a line: id,name,salary,department,position,email,hire_date,days_present,days_absent,half_days,overtime_hours
                line = f"{emp.employee_id},{emp.name},{emp.monthly_salary},{emp.department},{emp.position},{emp.email},{emp.hire_date},{emp.days_present},{emp.days_absent},{emp.half_days},{emp.overtime_hours}\n"
                file.write(line)
        print(f"Employee data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_employees_from_file(filename="employees.txt"):
    # Function to load employee data from a file
    # Returns a list of Employee objects
    employees = []
    try:
        with open(filename, 'r') as file:  # Open file in read mode
            for line in file:
                # Split the line by comma to get data
                data = line.strip().split(',')
                if len(data) >= 4:  # Minimum required fields
                    emp_id = data[0]
                    name = data[1]
                    salary = float(data[2])
                    
                    # Handle different file formats for backward compatibility
                    if len(data) == 4:  # Old format: id,name,salary,days_present
                        days_present = int(data[3])
                        emp = Employee(emp_id, name, salary)
                        emp.days_present = days_present
                    elif len(data) >= 11:  # New format: id,name,salary,department,position,email,hire_date,days_present,days_absent,half_days,overtime_hours
                        department = data[3]
                        position = data[4]
                        email = data[5]
                        hire_date = data[6]
                        days_present = int(data[7])
                        days_absent = int(data[8])
                        half_days = int(data[9])
                        overtime_hours = float(data[10])
                        
                        emp = Employee(emp_id, name, salary, department, position, email, hire_date)
                        emp.days_present = days_present
                        emp.days_absent = days_absent
                        emp.half_days = half_days
                        emp.overtime_hours = overtime_hours
                    
                    employees.append(emp)
        print(f"Employee data loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error loading data: {e}")
    return employees