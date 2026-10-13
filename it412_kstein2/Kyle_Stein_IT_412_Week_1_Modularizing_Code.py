"""
Kyle Stein
Walsh College - IT 410
Modified While Loops Assignment

This program collects information for up to five employees.
It validates user input using while loops and regular expressions,
stores the data in a list of dictionaries, and displays confirmation
messages for each employee entered.
"""
# For IT 412 Kyle Stein

import re   # Used for input validation


def get_employee_id():
    """
    Prompt the user for a validated employee ID.

    The employee ID must be numeric and contain at least 7 digits.
    The function continues to prompt until valid input is received.

    Returns:
        str: A validated employee ID.
    """
    while True:
        emp_id = input("Enter Employee ID (7 or more digits): ")
        if emp_id.isdigit() and len(emp_id) >= 7:
            return emp_id
        else:
            print("Invalid Employee ID. Please enter a numeric ID with at least 7 digits.")


def get_employee_name():
    """
    Prompt the user for a validated employee name.

    The name may contain only alphabetic characters and spaces.
    The function continues to prompt until valid input is received.

    Returns:
        str: A validated employee name.
    """
    while True:
        name = input("Enter Employee Name: ")
        if re.match(r'^[A-Za-z\s]+$', name):
            return name
        else:
            print("Invalid name. Please use only letters and spaces.")


def get_employee_email():
    """
    Prompt the user for a validated employee email address.

    The email may contain letters, numbers, spaces, '@', and '.'.
    This function uses simplified validation per assignment requirements.

    Returns:
        str: A validated email address.
    """
    while True:
        email = input("Enter Employee Email Address: ")
        if re.match(r'^[A-Za-z0-9@.\s]+$', email):
            return email
        else:
            print("Invalid email. Use only alphanumeric characters, '@', and '.'")


def get_employee_address():
    """
    Prompt the user for an optional employee address.

    If the user enters no value, a default message is stored.
    Valid characters include letters, numbers, spaces, commas, and periods.

    Returns:
        str: The employee address or 'No address provided'.
    """
    while True:
        addr = input("Enter Employee Address (optional): ")
        if addr == "" or re.match(r'^[A-Za-z0-9\s.,]+$', addr):
            return addr if addr != "" else "No address provided"
        else:
            print("Invalid address. Please use letters, numbers, commas, or periods only.")


def display_confirmation(name, emp_id, email, address):
    """
    Display a confirmation message for a single employee record.

    Args:
        name (str): Employee name.
        emp_id (str): Employee ID.
        email (str): Employee email address.
        address (str): Employee address or default message.

    Returns:
        None
    """
    print(f"\nHello, {name}. Your Employee ID is {emp_id}, and your email address is {email}.", end=" ")
    if address == "No address provided":
        print("You did not provide an address.")
    else:
        print(f"Your address is {address}.")


def main():
    """
    Main program logic.

    Collects information for up to five employees, stores each record
    in a list of dictionaries, and displays confirmation output.
    """
    employees = []

    for i in range(5):
        print(f"\nEntering information for Employee #{i + 1}")

        emp_id = get_employee_id()
        emp_name = get_employee_name()
        emp_email = get_employee_email()
        emp_address = get_employee_address()

        employee_record = {
            "Employee ID": emp_id,
            "Employee Name": emp_name,
            "Employee Email": emp_email,
            "Employee Address": emp_address
        }

        employees.append(employee_record)

        display_confirmation(emp_name, emp_id, emp_email, emp_address)

    print("\nFinal List of Employee Records:\n")
    for emp in employees:
        print(emp)


if __name__ == "__main__":
    main()
