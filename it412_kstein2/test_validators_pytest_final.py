# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

import pytest
from functions.validators import validate_phone, validate_zip, validate_state


@pytest.mark.parametrize("p", ["1234567890", "123-456-7890", "123.456.7890"])
def test_phone_ok(p):
    assert validate_phone(p) == p


@pytest.mark.parametrize("z", ["1234", "12345"])
def test_zip_ok(z):
    assert validate_zip(z) == z


@pytest.mark.parametrize("s", ["OH", "ca", "Tx"])
def test_state_ok(s):
    assert validate_state(s) in ("OH", "CA", "TX")
