# Kyle Stein 
# Walsh College
# IT 412
# 2/3/2026
# Week 4 & 5 Assignment

import unittest
from classes.inventory_item import InventoryItem
from classes.order import Order


class TestOrder(unittest.TestCase):

    def test_add_item_updates_total(self):
        order = Order(1)
        order.add_item(InventoryItem("Apple", 2, 1.00))
        self.assertEqual(order.total_price, 2.00)

    def test_remove_item(self):
        order = Order(2)
        order.add_item(InventoryItem("Apple", 1, 1.00))
        order.remove_item("Apple")
        self.assertEqual(order.total_price, 0.00)


if __name__ == "__main__":
    unittest.main()