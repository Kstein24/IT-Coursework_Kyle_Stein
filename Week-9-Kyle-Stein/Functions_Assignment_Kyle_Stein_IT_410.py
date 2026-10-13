# Kyle Stein
# Walsh College - IT 410
# Modified While Loops Assignment
# Uses functions to eliminate redundant code and improve organization


import re   # Used for input validation


# Function to get a validated numeric employee ID
def get_employee_id():
    while True:
        emp_id = input("Enter Employee ID (7 or more digits): ")
        if emp_id.isdigit() and len(emp_id) >= 7:
            return emp_id
        else:
            print("Invalid Employee ID. Please enter a numeric ID with at least 7 digits.")


# Function to get a validated employee name
def get_employee_name():
    while True:
        name = input("Enter Employee Name: ")
        if re.match(r'^[A-Za-z\s]+$', name):
            return name
        else:
            print("Invalid name. Please use only letters and spaces.")


# Function to get a validated employee email
def get_employee_email():
    while True:
        email = input("Enter Employee Email Address: ")
        if re.match(r'^[A-Za-z0-9@.\s]+$', email):
            return email
        else:
            print("Invalid email. Use only alphanumeric characters, '@', and '.'")


# Function to get an optional employee address
def get_employee_address():
    while True:
        addr = input("Enter Employee Address (optional): ")
        if addr == "" or re.match(r'^[A-Za-z0-9\s.,]+$', addr):
            return addr if addr != "" else "No address provided"
        else:
            print("Invalid address. Please use letters, numbers, commas, or periods only.")


# Function to display a confirmation message for each employee
def display_confirmation(name, emp_id, email, address):
    print(f"\nHello, {name}. Your Employee ID is {emp_id}, and your email address is {email}.", end=" ")
    if address == "No address provided":
        print("You did not provide an address.")
    else:
        print(f"Your address is {address}.")


# Main logic to collect up to 5 employees
employees = []

for i in range(5):
    print(f"\nEntering information for Employee #{i + 1}")

    emp_id = get_employee_id()
    emp_name = get_employee_name()
    emp_email = get_employee_email()
    emp_address = get_employee_address()

    # Store this employee’s data
    employee_record = {
        "Employee ID": emp_id,
        "Employee Name": emp_name,
        "Employee Email": emp_email,
        "Employee Address": emp_address
    }

    employees.append(employee_record)

    # Show confirmation
    display_confirmation(emp_name, emp_id, emp_email, emp_address)


# Display final employee list
print("\nFinal List of Employee Records:\n")
for emp in employees:
    print(emp)

