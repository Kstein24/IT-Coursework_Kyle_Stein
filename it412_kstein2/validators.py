# Kyle Stein 
# Walsh College
# IT 412
# 2/6/2026
# Week 6 & 7 Python Database

"""
validators.py

Validation rules (from assignment):
- Title: anything, but cannot be blank
- Author: letters, spaces, and only: , . ' -
- Qty: integer (0+)
- Signed: Y, N, or blank
- Prices: float if provided (promo optional, retail required)
"""

import re

AUTHOR_PATTERN = re.compile(r"^[A-Za-z\s,\.\'\-]+$")


def validate_title(title: str) -> str:
    title = title.strip()
    if not title:
        raise ValueError("Title cannot be blank.")
    return title


def validate_author(author: str) -> str:
    author = author.strip()
    if not author:
        raise ValueError("Author cannot be blank.")
    if not AUTHOR_PATTERN.fullmatch(author):
        raise ValueError("Author can only contain letters, spaces, and , . ' -")
    return author


def validate_qty(qty_text: str) -> int:
    qty_text = qty_text.strip()
    qty = int(qty_text)
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    return qty


def validate_signed(signed_text: str):
    s = signed_text.strip().upper()
    if s == "":
        return None
    if s not in ("Y", "N"):
        raise ValueError("Signed edition must be 'Y', 'N', or blank.")
    return s


def validate_price_optional(text: str):
    t = text.strip()
    if t == "":
        return None
    value = float(t)
    if value < 0:
        raise ValueError("Price cannot be negative.")
    return value


def validate_price_required(text: str) -> float:
    t = text.strip()
    value = float(t)
    if value < 0:
        raise ValueError("Price cannot be negative.")
    return value