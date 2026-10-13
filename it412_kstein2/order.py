# Kyle Stein 
# Walsh College
# IT 412
# 2/3/2026
# Week 4 & 5 Assignment

"""
Order class.

Stores order details and manages inventory items.
"""

from datetime import date
from classes.inventory_item import InventoryItem


class Order:
    """Represents a customer order."""

    def __init__(self, order_number: int):
        self.order_number = order_number
        self.order_date = date.today()
        self.items = []           # List of InventoryItem objects
        self.total_price = 0.0    # Total order cost

    def add_item(self, item: InventoryItem) -> None:
        # Ensure correct object type
        if not isinstance(item, InventoryItem):
            raise TypeError("Only InventoryItem objects can be added.")

        self.items.append(item)
        self._update_total()

    def remove_item(self, description: str) -> InventoryItem:
        # Remove item by description
        for index, item in enumerate(self.items):
            if item.description == description:
                removed_item = self.items.pop(index)
                self._update_total()
                return removed_item

        raise ValueError("Item not found in order.")

    def _update_total(self) -> None:
        # Recalculate order total
        self.total_price = sum(item.subtotal for item in self.items)
