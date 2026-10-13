# Kyle Stein
# Walsh College
# IT 410
# Program that collects and validates employee information 

# Import the regular expressions module for validation
import re

# Request Employee ID (must be a number that is 7 or more digits)
employee_id = input("Enter your Employee ID (7 or more digits): ")
if not (employee_id.isdigit() and len(employee_id) >= 7):
    print("Invalid Employee ID. Program terminated.")
    quit()

# Request Employee Name (must be letters only, cannot contain symbols or numbers)
employee_name = input("Enter your Employee Name: ")
if not re.match(r'^[A-Za-z\s]+$', employee_name):
    print("Invalid Employee Name. Program terminated.")
    quit()

# Request Employee Email Address (must be alphanumeric and cannot contain symbols like !\"@#$%^&*()_=+<>?/;:{}[])
employee_email = input("Enter your Employee Email Address: ")
if not re.match(r'^[A-Za-z0-9@.\s]+$', employee_email):
    print("Invalid Employee Email Address. Program terminated.")
    quit()

# Request Employee Address (optional; if provided, must be alphanumeric and cannot contain disallowed characters)
employee_address = input("Enter your Employee Address (optional): ")
if employee_address != "":
    if not re.match(r'^[A-Za-z0-9\s.,]+$', employee_address):
        print("Invalid Employee Address. Program terminated.")
        quit()

# Final print statement according to whether address was provided
print("\nHello,", employee_name + ".")
print("Your Employee ID is", employee_id + ", and your email address is", employee_email + ".", end=" ")

if employee_address == "":
    print("You did not provide an address.")
else:
    print("Your address is", employee_address + ".")
