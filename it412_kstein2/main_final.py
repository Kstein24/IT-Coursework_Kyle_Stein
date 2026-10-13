# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

"""
main.py

Customer Import Project
- Must not terminate unless user selects option #6
- name of database should be customer_db
"""

from classes.customer_app import CustomerApp


def print_menu():
    print("\n--- Customer Data Program ---")
    print("1. Import a new data file")
    print("2. Show data currently in a database table")
    print("3. Add a record to the database tables (adds to BOTH tables)")
    print("4. Edit a record")
    print("5. Delete a record")
    print("6. Quit the program")


def main():
    # IMPORTANT: XAMPP MySQL port is 3307 
    db_name = input("Enter your MySQL database name: ").strip()
    db_user = input("Enter MySQL username (default root): ").strip() or "root"
    db_password = input("Enter MySQL password (blank if none): ")

    app = CustomerApp(db_name=db_name, db_user=db_user, db_password=db_password)

    try:
        # Choose the two required application tables
        app.choose_two_tables()

        while True:
            print_menu()
            choice = input("Select an option (1-6): ").strip()

            if choice == "1":
                app.import_new_file()
            elif choice == "2":
                app.show_table_data()
            elif choice == "3":
                app.add_record()
            elif choice == "4":
                app.edit_record()
            elif choice == "5":
                app.delete_record()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid selection. Please choose 1-6.")

    finally:
        app.db.close()


if __name__ == "__main__":
    main()
