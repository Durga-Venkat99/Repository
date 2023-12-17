# SIMPLE CALCULATOR USING PYTHON

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculation
result = 0

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please enter +, -, *, or /.")

# Display the result
print("Result:", result)

print()
print(80*"-")
print()


# ENTERING EMPLOYEES DETAIL USING DICTIONARY PYTHON

employee_details = {}


def add_details():
    emp_name = input("enter name: ")
    emp_id = input("enter id: ")
    emp_age = int(input("enter age: "))
    emp_salary = int(input("enter salary: "))
    emp_email = input("enter email: ")
    emp_domain = input("enter domain: ")

    employee = {
        "name"  : emp_name,
        "I'D"   : emp_id,
        "Age"   : emp_age,
        "salary": emp_salary,
        "email" : emp_email,
        "domain": emp_domain
    }
    employee_details[emp_id] = employee
def employee_id():
    emp_id = input("enter employee_id for details: ")

    if emp_id in employee_details:
        employee = employee_details[emp_id]
        print("employee details: ")
        for key,value in employee.items():
            print(f"{key}:{value}")
    else:
        print("employee id is not found")
    
while True:
    print("Employee Management System")
    print("1. Add Employee")
    print("2. enter the employee details")
    print("3. Exit")

    choice = input("enter choice: ")

    if choice == '1':
        add_details()
    elif choice == '2':
        employee_id()
    elif choice == '3':
        break
    else:
        print("enter the invalid details")
print("program existed")