# write a python program that allows you to add an employee with domain, name, empid, and email details using user input ?


print("Using python dictionary add employee details")
print("--------------------------------------------")
print()

employee_details = {}

def add_employee():
    Domain = input("enter domain: ")
    name = input("enter name: ")
    emp_id = input("enter id : ")
    email = input("enter email: ")

    employee = {
        "Domain" : Domain,
        "Name"   : name,
        "Emp_id" : emp_id,
        "Email"  : email
        }
    employee_details[emp_id] = employee

def print_emp_details():
    emp_id = input("Enter the employee details: ")

    if emp_id in employee_details:
        employee = employee_details[emp_id]
        print("employee details: ")
        for key, value in employee.items():
            print(f"{key}:{value}")
    else:
        print("empl_id is not found in list")

while True:
    print("\nOptions:")
    print("1. Add Employee")
    print("2. Print Employee Details")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        print_emp_details()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Program exited.")

