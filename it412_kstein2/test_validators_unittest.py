# Kyle Stein 
# Walsh College
# IT 412
# 2/6/2026
# Week 6 & 7 Python Database

import unittest
from functions.validators import (
    validate_title,
    validate_author,
    validate_qty,
    validate_signed,
    validate_price_optional,
    validate_price_required
)


class TestValidators(unittest.TestCase):

    def test_title_ok(self):
        self.assertEqual(validate_title("Dune"), "Dune")

    def test_title_blank_raises(self):
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_author_ok(self):
        self.assertEqual(validate_author("Mary-Jane O'Neil, Jr."), "Mary-Jane O'Neil, Jr.")

    def test_author_invalid_raises(self):
        with self.assertRaises(ValueError):
            validate_author("Bob123")

    def test_qty_ok(self):
        self.assertEqual(validate_qty("10"), 10)

    def test_qty_negative_raises(self):
        with self.assertRaises(ValueError):
            validate_qty("-1")

    def test_signed_blank(self):
        self.assertIsNone(validate_signed(""))

    def test_signed_y(self):
        self.assertEqual(validate_signed("y"), "Y")

    def test_price_optional_blank(self):
        self.assertIsNone(validate_price_optional(""))

    def test_price_required_ok(self):
        self.assertEqual(validate_price_required("19.99"), 19.99)


if __name__ == "__main__":
    unittest.main()
