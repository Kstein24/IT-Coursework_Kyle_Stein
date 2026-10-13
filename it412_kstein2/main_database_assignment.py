# Kyle Stein 
# Walsh College
# IT 412
# 2/6/2026
# Week 6 & 7 Python Database

"""
main.py

Family Bookstore Inventory Program (PyMySQL).
Program loop continues until user selects option #6.
"""

from classes.inventory_db import InventoryDB
from functions.ui_helpers import prompt_int
from functions.validators import (
    validate_title,
    validate_author,
    validate_qty,
    validate_signed,
    validate_price_optional,
    validate_price_required
)


def print_menu():
    print("\n--- Family Bookstore Inventory ---")
    print("1. Show all books")
    print("2. Add a Book")
    print("3. Record a book sale")
    print("4. Edit book details")
    print("5. Remove a book")
    print("6. Exit program")


def show_all_books(inv: InventoryDB):
    """Print each row using a loop (assignment requirement)."""
    try:
        books = inv.fetch_all_books()
        if not books:
            print("No books found.")
            return

        for b in books:
            signed = b["signed_edition"] if b["signed_edition"] else "(blank)"
            promo = f"${float(b['promo_price']):.2f}" if b["promo_price"] is not None else "(none)"
            retail = f"${float(b['retail_price']):.2f}"

            print("\n-------------------------")
            print(f"ID: {b['book_id']}")
            print(f"Title: {b['title']}")
            print(f"Author: {b['author']}")
            print(f"Quantity on hand: {b['qty_on_hand']}")
            print(f"Signed edition: {signed}")
            print(f"Promotional price: {promo}")
            print(f"Retail price: {retail}")

    except Exception as ex:
        print(f"Error showing books: {ex}")


def add_book(inv: InventoryDB):
    """Add a book after validating all fields."""
    while True:
        try:
            title = validate_title(input("Book Title: "))
            author = validate_author(input("Book Author: "))
            qty = validate_qty(input("Quantity on hand (integer): "))
            signed = validate_signed(input("Signed edition? (Y/N/blank): "))
            promo = validate_price_optional(input("Promotional price (float/blank): "))
            retail = validate_price_required(input("Retail price (float): "))

            inv.add_book(title, author, qty, signed, promo, retail)
            print("Book added successfully.")
            return

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as ex:
            print(f"Error adding book: {ex}")
            return


def record_sale(inv: InventoryDB):
    """Record a book sale and prevent negative inventory."""
    try:
        book_id = prompt_int("Enter Book ID sold: ")
        book = inv.fetch_book_by_id(book_id)
        if not book:
            print("That Book ID does not exist.")
            return

        qty_sold = validate_qty(input("How many copies were sold? (integer): "))
        if qty_sold == 0:
            print("Sale quantity must be at least 1.")
            return

        new_qty = inv.record_sale(book_id, qty_sold)
        print(f"Sale recorded. New quantity on hand: {new_qty}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as ex:
        print(f"Error recording sale: {ex}")


def edit_book(inv: InventoryDB):
    """Ask which field to edit, then validate just that field."""
    try:
        book_id = prompt_int("Enter Book ID to edit: ")
        book = inv.fetch_book_by_id(book_id)
        if not book:
            print("That Book ID does not exist.")
            return

        print("\nEditable fields:")
        print("title, author, qty_on_hand, signed_edition, promo_price, retail_price")
        field = input("Which field would you like to edit? ").strip()

        if field == "title":
            value = validate_title(input("New title: "))
        elif field == "author":
            value = validate_author(input("New author: "))
        elif field == "qty_on_hand":
            value = validate_qty(input("New quantity (integer): "))
        elif field == "signed_edition":
            value = validate_signed(input("New signed edition (Y/N/blank): "))
        elif field == "promo_price":
            value = validate_price_optional(input("New promo price (float/blank): "))
        elif field == "retail_price":
            value = validate_price_required(input("New retail price (float): "))
        else:
            print("Invalid field.")
            return

        inv.update_field(book_id, field, value)
        print("Book updated successfully.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as ex:
        print(f"Error editing book: {ex}")


def remove_book(inv: InventoryDB):
    """Confirm deletion before removing a book."""
    try:
        book_id = prompt_int("Enter Book ID to remove: ")
        book = inv.fetch_book_by_id(book_id)
        if not book:
            print("That Book ID does not exist.")
            return

        print(f"\nDelete: ID {book['book_id']} - {book['title']} by {book['author']}")
        confirm = input("Type YES to confirm deletion: ").strip().upper()
        if confirm != "YES":
            print("Deletion cancelled.")
            return

        inv.delete_book(book_id)
        print("Book removed successfully.")

    except Exception as ex:
        print(f"Error removing book: {ex}")


def main():
    inv = InventoryDB()

    try:
        while True:
            print_menu()
            choice = input("Select an option (1-6): ").strip()

            if choice == "1":
                show_all_books(inv)
            elif choice == "2":
                add_book(inv)
            elif choice == "3":
                record_sale(inv)
            elif choice == "4":
                edit_book(inv)
            elif choice == "5":
                remove_book(inv)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid selection. Choose 1-6.")
    finally:
        inv.close()


if __name__ == "__main__":
    main()
