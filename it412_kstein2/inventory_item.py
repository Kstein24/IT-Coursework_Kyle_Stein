# Kyle Stein 
# Walsh College
# IT 412
# 2/3/2026
# Week 4 & 5 Assignment

"""
InventoryItem class.

Stores item description, quantity, and pricing information.
"""

class InventoryItem:
    """Represents an inventory item."""

    def __init__(self, description: str, quantity: int, price):
        # Use setters so validation is enforced on creation
        self.description = description
        self.quantity = quantity
        self.price = price

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        # Description must be a string
        if not isinstance(value, str):
            raise TypeError("Description must be a string.")

        # Must contain only alphanumeric characters
        if not value.isalnum():
            raise ValueError("Description must be alphanumeric only.")

        self._description = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        # Quantity must be a whole number
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Quantity must be an integer.")

        if value < 0:
            raise ValueError("Quantity cannot be negative.")

        self._quantity = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        # Pricing must be convertible to float
        try:
            float_value = float(value)
        except (TypeError, ValueError) as exc:
            raise TypeError("Price must be a float value.") from exc

        if float_value < 0:
            raise ValueError("Price cannot be negative.")

        self._price = float_value

    @property
    def subtotal(self) -> float:
        # Total cost for this item
        return self.quantity * self.price
