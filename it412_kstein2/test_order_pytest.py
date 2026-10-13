# Kyle Stein 
# Walsh College
# IT 412
# 2/3/2026
# Week 4 & 5 Assignment

import pytest
from classes.inventory_item import InventoryItem
from classes.order import Order


def test_order_total():
    order = Order(10)
    order.add_item(InventoryItem("Apple", 2, 1.00))
    assert order.total_price == 2.00