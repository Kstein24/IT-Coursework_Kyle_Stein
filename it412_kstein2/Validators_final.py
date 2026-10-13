# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

"""
validators.py

Raises ValueError with clear messages when invalid.
"""

import re

# First/Last name: letters with spaces + ' and -
NAME_RE = re.compile(r"^[A-Za-z]+(?:[A-Za-z\s'\-]*[A-Za-z])?$")

# Address: primarily alphanumeric; allow spaces and: # , . - & ( ) \ /
ADDRESS_RE = re.compile(r"^[A-Za-z0-9]+(?:[A-Za-z0-9\s#,\.\-&()\\/]*[A-Za-z0-9])?$")

# Email: alphanumeric + allowed: . - _ @ +
EMAIL_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.\-_@+]*[A-Za-z0-9]$")

# Phone: either 10 digits OR 12 with separators like 123-456-7890 or 123.456.7890
PHONE_10_RE = re.compile(r"^\d{10}$")
PHONE_12_RE = re.compile(r"^\d{3}[-.]\d{3}[-.]\d{4}$")

# State abbreviations list 
VALID_STATES = {
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
    "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
}

# City must not contain these 
CITY_BAD_CHARS = set('!"@$%^&*_=+<>?;:[]{}~`')


def validate_name(text: str, field_name: str) -> str:
    """Validate first/last names."""
    val = text.strip()
    if not val:
        raise ValueError(f"{field_name} cannot be blank.")
    if not NAME_RE.fullmatch(val):
        raise ValueError(f"{field_name} must be letters/spaces and may include ' or -.")
    return val


def validate_company(text: str) -> str:
    """Company may be almost anything, but must NOT contain: ` ~ ^ \\ { } | < >"""
    val = text.strip()
    if not val:
        raise ValueError("Company name cannot be blank.")
    forbidden = set(r"`~^\{}|<>\\")
    if any(ch in forbidden for ch in val):
        raise ValueError("Company name contains forbidden character (` ~ ^ \\ { } | < >).")
    return val


def validate_address(text: str) -> str:
    """Address must be primarily alphanumeric; allows spaces and # , . - & ( ) \\ /"""
    val = text.strip()
    if not val:
        raise ValueError("Address cannot be blank.")
    if not ADDRESS_RE.fullmatch(val):
        raise ValueError("Address contains invalid characters.")
    return val


def validate_city(text: str) -> str:
    """City: letters w/spaces allowed; cannot contain certain symbols."""
    val = text.strip()
    if not val:
        raise ValueError("City cannot be blank.")
    if any(ch in CITY_BAD_CHARS for ch in val):
        raise ValueError("City contains forbidden symbol characters.")
    if not re.fullmatch(r"[A-Za-z\s]+", val):
        raise ValueError("City must be letters and spaces only.")
    return val


def validate_county(text: str) -> str:
    """County: keep simple letters/spaces allowed."""
    val = text.strip()
    if not val:
        raise ValueError("County cannot be blank.")
    if not re.fullmatch(r"[A-Za-z\s\-]+", val):
        raise ValueError("County contains invalid characters.")
    return val


def validate_state(text: str) -> str:
    """State must be one of the valid abbreviations list."""
    val = text.strip().upper()
    if val not in VALID_STATES:
        raise ValueError("State must be a valid 2-letter US abbreviation.")
    return val


def validate_zip(text: str) -> str:
    """ZIP must be 4 or 5 digits."""
    val = text.strip()
    if not re.fullmatch(r"\d{4,5}", val):
        raise ValueError("ZIP must be 4 or 5 digits.")
    return val


def validate_phone(text: str, allow_blank=True):
    """Phone must be digits and - or . ; either 10 digits or 12 with separators."""
    val = text.strip()
    if val == "" and allow_blank:
        return None
    if PHONE_10_RE.fullmatch(val) or PHONE_12_RE.fullmatch(val):
        return val
    raise ValueError("Phone must be 10 digits or formatted like 123-456-7890 / 123.456.7890.")


def validate_email(text: str) -> str:
    """Email must be primarily alphanumeric and may contain . - _ @ +"""
    val = text.strip()
    if not val:
        raise ValueError("Email cannot be blank.")
    if not EMAIL_RE.fullmatch(val):
        raise ValueError("Email contains invalid characters.")
    return val