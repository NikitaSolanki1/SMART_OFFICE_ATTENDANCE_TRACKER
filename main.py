# main.py
# This is the entry point of the project.
# It provides a menu-driven command-line interface (CLI) for the user to interact with the system.
# The program flow is simple: display menu, get user choice, perform action, repeat until exit.

from company import Company
from employee import Employee
from file_handler import save_employees_to_file, load_employees_from_file

def generate_attendance_report(employees):
    # Function to generate a summary attendance report
    if not employees:
        print("No employees to report on.")
        return
    
    print("\n--- Attendance Report ---")
    print(f"{'ID':<10} {'Name':<20} {'Department':<15} {'Present':<8} {'Half':<6} {'Absent':<7} {'Overtime':<9} {'Salary':<10}")
    print("-" * 90)
    
    total_present = 0
    total_half = 0
    total_absent = 0
    total_overtime = 0
    total_salary = 0
    
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"{emp.employee_id:<10} {emp.name:<20} {emp.department:<15} {emp.days_present:<8} {emp.half_days:<6} {emp.days_absent:<7} {emp.overtime_hours:<9.1f} ${salary:<9.2f}")
        
        total_present += emp.days_present
        total_half += emp.half_days
        total_absent += emp.days_absent
        total_overtime += emp.overtime_hours
        total_salary += salary
    
    print("-" * 90)
    print(f"{'TOTAL':<10} {'':<20} {'':<15} {total_present:<8} {total_half:<6} {total_absent:<7} {total_overtime:<9.1f} ${total_salary:<9.2f}")

def main():
    # Create a company object
    company = Company("Nikerio")

    # Load existing data if available
    company.employees = load_employees_from_file()

    while True:  # Loop until user chooses to exit
        print("\n--- Nikerio Attendance and Salary Tracker ---")
        print("1. Add new employee")
        print("2. Mark attendance")
        print("3. Add overtime hours")
        print("4. View employee details")
        print("5. View all employees")
        print("6. Generate attendance report")
        print("7. Save data to file")
        print("8. Load data from file")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            # Add new employee
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            salary = float(input("Enter monthly salary: "))
            department = input("Enter department (default: General): ").strip() or "General"
            position = input("Enter position (default: Employee): ").strip() or "Employee"
            email = input("Enter email (leave blank for auto-generated): ").strip()
            email = email if email else None
            emp = Employee(emp_id, name, salary, department, position, email)
            company.add_employee(emp)

        elif choice == '2':
            # Mark attendance
            emp_id = input("Enter employee ID to mark attendance: ")
            attendance_type = input("Enter attendance type (full/half/absent) [default: full]: ").strip().lower()
            if attendance_type not in ['full', 'half', 'absent']:
                attendance_type = 'full'
            
            for emp in company.employees:
                if emp.employee_id == emp_id:
                    emp.mark_attendance(attendance_type)
                    break
            else:
                print("Employee not found.")

        elif choice == '3':
            # Add overtime hours
            emp_id = input("Enter employee ID to add overtime: ")
            try:
                hours = float(input("Enter overtime hours: "))
                for emp in company.employees:
                    if emp.employee_id == emp_id:
                        emp.add_overtime(hours)
                        break
                else:
                    print("Employee not found.")
            except ValueError:
                print("Invalid number of hours.")

        elif choice == '4':
            # View employee details
            emp_id = input("Enter employee ID to view details: ")
            for emp in company.employees:
                if emp.employee_id == emp_id:
                    emp.show_details()
                    salary = emp.calculate_salary()
                    print(f"Earned Salary: ${salary:.2f}")
                    break
            else:
                print("Employee not found.")

        elif choice == '5':
            # View all employees
            company.list_employees()

        elif choice == '6':
            # Generate attendance report
            generate_attendance_report(company.employees)

        elif choice == '7':
            # Save data to file
            save_employees_to_file(company.employees)

        elif choice == '8':
            # Load data from file
            company.employees = load_employees_from_file()

        elif choice == '9':
            # Exit
            print("logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Call the main function when the script is run