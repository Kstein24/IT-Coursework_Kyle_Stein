# Kyle Stein 
# Walsh College
# IT 412
# 1/22/2026
# Week 2 & 3 Files And Exceptions

"""
Main program entry point.

Contains only menu logic and delegates all real work
to functions and classes (per assignment instructions).
"""

from pathlib import Path

from classes.server_manager import ServerManager
from functions.cli import prompt_choice, print_header
from functions.primary import load_primary_config, edit_primary_config


def main() -> None:
    base_dir = Path(__file__).resolve().parent

    primary = load_primary_config(base_dir)
    manager = ServerManager(base_dir)

    while True:
        print_header("Server Configuration Manager")

        if not manager.has_servers():
            print("1. Add a new server")
            print("2. Modify Primary Configuration")
            print("3. Exit")

            choice = prompt_choice("Choose: ", ["1", "2", "3"])

            if choice == "1":
                manager.add_server(primary)
            elif choice == "2":
                primary = edit_primary_config(base_dir, primary)
            else:
                break
        else:
            print("1. Add server")
            print("2. Modify server")
            print("3. Delete server")
            print("4. Modify primary config")
            print("5. Save servers")
            print("6. Exit")

            choice = prompt_choice("Choose: ", ["1", "2", "3", "4", "5", "6"])

            if choice == "1":
                manager.add_server(primary)
            elif choice == "2":
                manager.modify_server()
            elif choice == "3":
                manager.delete_server()
            elif choice == "4":
                primary = edit_primary_config(base_dir, primary)
            elif choice == "5":
                manager.save_servers()
            else:
                break


if __name__ == "__main__":
    main()
