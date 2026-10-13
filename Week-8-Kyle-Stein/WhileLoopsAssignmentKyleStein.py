# Kyle Stein
# Walsh College
# IT 410
# Program that collects information for up to 5 employees
# Includes validation and stores data as a list of dictionaries


import re  # Used for input validation

# Initialize an empty list to store employee dictionaries
employees = []

# Loop to collect up to 5 employees’ data
for i in range(5):
    print(f"\nEntering information for Employee #{i + 1}")
    
    # Get valid Employee ID (must be 7 or more digits)
    while True:
        employee_id = input("Enter Employee ID (7 or more digits): ")
        if employee_id.isdigit() and len(employee_id) >= 7:
            break
        else:
            print("Invalid Employee ID. Please enter a numeric ID with at least 7 digits.")

    # Get valid Employee Name (letters only)
    while True:
        employee_name = input("Enter Employee Name: ")
        if re.match(r'^[A-Za-z\s]+$', employee_name):
            break
        else:
            print("Invalid name. Please use only letters and spaces.")
    
    # Get valid Employee Email Address (alphanumeric and @, . allowed)
    while True:
        employee_email = input("Enter Employee Email Address: ")
        if re.match(r'^[A-Za-z0-9@.\s]+$', employee_email):
            break
        else:
            print("Invalid email. Use only alphanumeric characters, '@', and '.'")
    
    # Get optional Employee Address (alphanumeric and basic punctuation allowed)
    while True:
        employee_address = input("Enter Employee Address (optional): ")
        if employee_address == "" or re.match(r'^[A-Za-z0-9\s.,]+$', employee_address):
            break
        else:
            print("Invalid address. Please use letters, numbers, commas, or periods only.")
    
    # Create dictionary entry for this employee
    employee_info = {
        "Employee ID": employee_id,
        "Employee Name": employee_name,
        "Employee Email": employee_email,
        "Employee Address": employee_address if employee_address != "" else "No address provided"
    }
    
    # Add dictionary to list
    employees.append(employee_info)

    # Confirmation message for this employee
    print(f"\nHello, {employee_name}. Your Employee ID is {employee_id}, and your email address is {employee_email}.", end=" ")
    if employee_address == "":
        print("You did not provide an address.")
    else:
        print(f"Your address is {employee_address}.")

# Print final list of employee dictionaries
print("\nFinal List of Employee Records:\n")
for emp in employees:
    print(emp)
