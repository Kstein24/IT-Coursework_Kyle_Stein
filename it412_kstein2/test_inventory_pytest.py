# Kyle Stein 
# Walsh College
# IT 412
# 2/3/2026
# Week 4 & 5 Assignment

import pytest
from classes.inventory_item import InventoryItem


def test_valid_item():
    item = InventoryItem("Apple", 2, 1.25)
    assert item.subtotal == 2.50


def test_invalid_description():
    with pytest.raises(ValueError):
        InventoryItem("Red Apple", 1, 1.00)
