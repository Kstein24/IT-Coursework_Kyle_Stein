# Kyle Stein
# IT 410 - Classes Assignment
# Program collects validated student and instructor information using classes and inheritance.


import re



# Validator Class
# Contains static validation methods for all input fields.

class Validator:

    @staticmethod
    def validate_student_id(sid):
        return sid.isdigit() and len(sid) >= 7

    @staticmethod
    def validate_instructor_id(iid):
        return iid.isdigit() and len(iid) <= 5

    @staticmethod
    def validate_name(name):
        return bool(re.match(r'^[A-Za-z]+$', name))

    @staticmethod
    def validate_email(email):
        return bool(re.match(r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]+$', email))

    @staticmethod
    def validate_program(program):
        return bool(re.match(r'^[A-Za-z]+$', program))

    @staticmethod
    def validate_institution(inst):
        return bool(re.match(r'^[A-Za-z]+$', inst))

    @staticmethod
    def validate_degree(degree):
        return bool(re.match(r'^[A-Za-z]+$', degree))



# Base Class: ValidatedInformation
# Holds shared fields and methods for all individuals.

class ValidatedInformation:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        print("Name:", self.name)
        print("Email:", self.email)



# Student Class
# Inherits shared fields and adds student specific attributes.

class Student(ValidatedInformation):

    def __init__(self, name, email, student_id, program):
        super().__init__(name, email)
        self.student_id = student_id
        self.program = program

    def displayInformation(self):
        print("\nStudent Record")
        print("Student ID:", self.student_id)
        super().displayInformation()
        print("Program of Study:", self.program)



# Instructor Class
# Inherits shared fields and adds instructor specific attributes.

class Instructor(ValidatedInformation):

    def __init__(self, name, email, instructor_id, last_institution, degree):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.last_institution = last_institution
        self.degree = degree

    def displayInformation(self):
        print("\nInstructor Record")
        print("Instructor ID:", self.instructor_id)
        super().displayInformation()
        print("Last Institution Graduated From:", self.last_institution)
        print("Highest Degree Earned:", self.degree)


# List to store all student and instructor objects
college_records = []

print("College Records System\n")


# Main Input Loop
# Repeats until the user chooses to stop.

while True:

    user_type = input("Is this individual a Student or Instructor? ").strip().lower()
    while user_type not in ["student", "instructor"]:
        user_type = input("Enter Student or Instructor: ").strip().lower()

    # Shared fields
    name = input("Enter individual's name (letters only): ")
    while not Validator.validate_name(name):
        name = input("Invalid. Enter name again: ")

    email = input("Enter individual's email address: ")
    while not Validator.validate_email(email):
        email = input("Invalid email. Enter again: ")

    # Student logic
    if user_type == "student":
        student_id = input("Enter Student ID (7 or more digits): ")
        while not Validator.validate_student_id(student_id):
            student_id = input("Invalid. Enter Student ID again: ")

        program = input("Enter Program of Study (letters only): ")
        while not Validator.validate_program(program):
            program = input("Invalid. Enter Program of Study again: ")

        college_records.append(Student(name, email, student_id, program))

    # Instructor logic
    else:
        instructor_id = input("Enter Instructor ID (5 or fewer digits): ")
        while not Validator.validate_instructor_id(instructor_id):
            instructor_id = input("Invalid. Enter Instructor ID again: ")

        institution = input("Enter last institution graduated from (letters only): ")
        while not Validator.validate_institution(institution):
            institution = input("Invalid. Enter institution again: ")

        degree = input("Enter highest degree earned (letters only): ")
        while not Validator.validate_degree(degree):
            degree = input("Invalid. Enter degree again: ")

        college_records.append(Instructor(name, email, instructor_id, institution, degree))

    another = input("Would you like to enter another individual? (yes or no): ").strip().lower()
    if another != "yes":
        break



# Output Section
# Displays all stored records using each object's method.

print("\nFinal College Records\n")
for record in college_records:
    record.displayInformation()
    print()
