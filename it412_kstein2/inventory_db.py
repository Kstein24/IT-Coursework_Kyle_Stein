# Kyle Stein 
# Walsh College
# IT 412
# 2/6/2026
# Week 6 & 7 Python Database

"""
inventory_db.py

CRUD + sales logic for bookstore inventory.
Uses Database class (PyMySQL underneath).
"""

from classes.database import Database


class InventoryDB:
    """Handles all inventory database operations."""

    def __init__(self):
        # Change credentials if your MySQL login differs
        self.db = Database(user="root", password="Pabloshadow24", database="bookstore_db")

    def close(self):
        """Close DB connection."""
        self.db.close()

    def fetch_all_books(self):
        """Get all books."""
        return self.db.query_all("SELECT * FROM books ORDER BY book_id")

    def fetch_book_by_id(self, book_id: int):
        """Get one book by id."""
        return self.db.query_one("SELECT * FROM books WHERE book_id = %s", (book_id,))

    def add_book(self, title, author, qty, signed, promo, retail):
        """Insert a new book."""
        sql = """
        INSERT INTO books (title, author, qty_on_hand, signed_edition, promo_price, retail_price)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        return self.db.execute(sql, (title, author, qty, signed, promo, retail))

    def update_field(self, book_id: int, field: str, value):
        """Update a single field (column) for a book."""
        allowed = {"title", "author", "qty_on_hand", "signed_edition", "promo_price", "retail_price"}
        if field not in allowed:
            raise ValueError("Invalid field name.")

        sql = f"UPDATE books SET {field} = %s WHERE book_id = %s"
        return self.db.execute(sql, (value, book_id))

    def delete_book(self, book_id: int):
        """Delete a book by id."""
        return self.db.execute("DELETE FROM books WHERE book_id = %s", (book_id,))

    def record_sale(self, book_id: int, qty_sold: int):
        """
        Record a sale by subtracting qty_sold.
        Prevents inventory going negative.
        """
        book = self.fetch_book_by_id(book_id)
        if not book:
            raise ValueError("Book ID not found.")

        on_hand = book["qty_on_hand"]
        if qty_sold <= 0:
            raise ValueError("Quantity sold must be at least 1.")
        if qty_sold > on_hand:
            raise ValueError(f"Not enough inventory. On hand: {on_hand}")

        new_qty = on_hand - qty_sold
        self.update_field(book_id, "qty_on_hand", new_qty)
        return new_qty
