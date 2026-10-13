# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

import unittest
from functions.validators import (
    validate_name, validate_company, validate_address, validate_city, validate_state,
    validate_zip, validate_phone, validate_email
)


class TestValidators(unittest.TestCase):
    def test_name_ok(self):
        self.assertEqual(validate_name("O'Neil", "First name"), "O'Neil")

    def test_state_ok(self):
        self.assertEqual(validate_state("oh"), "OH")

    def test_zip_ok(self):
        self.assertEqual(validate_zip("8014"), "8014")
        self.assertEqual(validate_zip("70116"), "70116")

    def test_phone_ok(self):
        self.assertEqual(validate_phone("504-621-8927"), "504-621-8927")
        self.assertEqual(validate_phone("5046218927"), "5046218927")

    def test_email_ok(self):
        self.assertEqual(validate_email("a_b-c+1@test.com"), "a_b-c+1@test.com")

    def test_company_forbidden(self):
        with self.assertRaises(ValueError):
            validate_company("Bad < Company")


if __name__ == "__main__":
    unittest.main()
