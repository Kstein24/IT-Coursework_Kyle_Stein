# Kyle Stein 
# Walsh College
# IT 412
# 2/3/2026
# Week 4 & 5 Assignment

import unittest
from classes.inventory_item import InventoryItem


class TestInventoryItem(unittest.TestCase):

    def test_valid_item(self):
        item = InventoryItem("Apple", 2, 1.50)
        self.assertEqual(item.subtotal, 3.00)

    def test_invalid_description(self):
        with self.assertRaises(ValueError):
            InventoryItem("Red Apple", 1, 1.00)

    def test_invalid_quantity(self):
        with self.assertRaises(TypeError):
            InventoryItem("Apple", 1.5, 1.00)


if __name__ == "__main__":
    unittest.main()
