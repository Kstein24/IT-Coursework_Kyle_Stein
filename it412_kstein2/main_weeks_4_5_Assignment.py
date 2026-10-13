# Kyle Stein 
# Walsh College
# IT 412
# 2/3/2026
# Week 4 & 5 Assignment

"""
Main program to demonstrate the cash register system.
"""
import sys
from pathlib import Path

# Add project root to Python import path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from classes.inventory_item import InventoryItem
from classes.order import Order


def main() -> None:
    # Create a new order
    order = Order(101)

    # Create inventory items
    item1 = InventoryItem("Apple", 3, 0.99)
    item2 = InventoryItem("Milk", 2, 1.79)

    # Add items to the order
    order.add_item(item1)
    order.add_item(item2)

    # Remove one item
    order.remove_item("Apple")

    # Display final order total
    print(f"Order Number: {order.order_number}")
    print(f"Order Date: {order.order_date}")
    print(f"Total Price: ${order.total_price:.2f}")


if __name__ == "__main__":
    main()
