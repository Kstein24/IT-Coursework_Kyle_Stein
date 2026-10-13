# Kyle Stein 
# Walsh College
# IT 412
# 2/6/2026
# Week 6 & 7 Python Database

import pytest
from functions.validators import (
    validate_title,
    validate_author,
    validate_qty,
    validate_signed,
    validate_price_optional,
    validate_price_required
)


def test_title_ok():
    assert validate_title("1984") == "1984"


def test_title_blank_raises():
    with pytest.raises(ValueError):
        validate_title("")


@pytest.mark.parametrize("name", ["John Smith", "Mary-Jane O'Neil", "A. B. Author", "Last, First"])
def test_author_ok(name):
    assert validate_author(name) == name


@pytest.mark.parametrize("bad", ["Bob123", "Jane@", "Name!"])
def test_author_bad_raises(bad):
    with pytest.raises(ValueError):
        validate_author(bad)


@pytest.mark.parametrize("text, expected", [("0", 0), ("7", 7), (" 12 ", 12)])
def test_qty_ok(text, expected):
    assert validate_qty(text) == expected


def test_signed_blank_returns_none():
    assert validate_signed("") is None


def test_price_optional_blank_returns_none():
    assert validate_price_optional("") is None


def test_price_required_ok():
    assert validate_price_required("5.25") == 5.25
