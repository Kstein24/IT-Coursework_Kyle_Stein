# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

"""
customer_app.py

Core app:
- Parses customer_export.txt style data (##value## wrapped)
- Cleans and deduplicates
- Exports:
  - customer_phone.json (first_name + phone numbers ONLY)
  - customer_location.csv (first_name,last_name,county,state ONLY)
- Loads into 2 DB tables selected by the user (no schema changes)
"""

from __future__ import annotations

import json
import csv
import re
from pathlib import Path

from classes.database import Database
from functions.file_tools import backup_if_exists
from functions.validators import (
    validate_name, validate_company, validate_address, validate_city, validate_county,
    validate_state, validate_zip, validate_phone, validate_email
)


TOKEN_RE = re.compile(r"##(.*?)##")


class CustomerApp:
    """Implements required menu operations and DB/file work."""

    def __init__(self, db_name: str, db_user: str = "root", db_password: str = "", host="127.0.0.1", port=3307):
        # IMPORTANT: XAMPP MySQL port is 3307
        self.db = Database(host=host, user=db_user, password=db_password, database=db_name, port=port)

        # Two “application tables” (selected by user once, then used for options 2–5)
        self.table_a = None
        self.table_b = None

        # In-memory loaded records (list[dict])
        self.records: list[dict] = []

    # -------------------------
    # Parsing / cleaning
    # -------------------------
    def parse_export_file(self, file_path: Path) -> list[dict]:
        """Parse customer_export.txt style file into list of dicts."""
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
        if not lines:
            return []

        # Extract headers from first line using ##...## token capture
        headers = TOKEN_RE.findall(lines[0])
        headers = [h.strip() for h in headers if h.strip()]

        parsed = []
        for line in lines[1:]:
            tokens = TOKEN_RE.findall(line)
            # Make tokens list same length as headers (pad/truncate)
            values = [t.strip() for t in tokens]
            if len(values) < len(headers):
                values += [""] * (len(headers) - len(values))
            if len(values) > len(headers):
                values = values[:len(headers)]

            row = dict(zip(headers, values))
            parsed.append(row)

        return parsed

    def dedupe_records(self, rows: list[dict]) -> list[dict]:
        """Attempt to remove duplicates (full normalized row key)."""
        seen = set()
        unique = []
        for r in rows:
            # Normalize key (lower/strip) for stable dedupe
            key = tuple((k, (r.get(k) or "").strip().lower()) for k in sorted(r.keys()))
            if key not in seen:
                seen.add(key)
                unique.append(r)
        return unique

    # -------------------------
    # Required file outputs
    # -------------------------
    def export_phone_json(self, out_path: Path) -> None:
        """
        Create customer_phone.json:
        ONLY first_name and phone numbers associated with that record.
        """
        backup_if_exists(out_path)

        payload = []
        for r in self.records:
            phones = []
            p1 = (r.get("phone1") or "").strip()
            p2 = (r.get("phone2") or "").strip()
            if p1:
                phones.append(p1)
            if p2:
                phones.append(p2)

            payload.append({
                "first_name": (r.get("first_name") or "").strip(),
                "phones": phones
            })

        out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def export_location_csv(self, out_path: Path) -> None:
        """
        Create customer_location.csv:
        ONLY first_name,last_name,county,state
        """
        backup_if_exists(out_path)

        with out_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["first_name", "last_name", "county", "state"])
            writer.writeheader()
            for r in self.records:
                writer.writerow({
                    "first_name": (r.get("first_name") or "").strip(),
                    "last_name": (r.get("last_name") or "").strip(),
                    "county": (r.get("county") or "").strip(),
                    "state": (r.get("state") or "").strip()
                })

    # -------------------------
    # DB helpers
    # -------------------------
    def list_user_tables(self) -> list[str]:
        """List tables in the current database."""
        rows = self.db.query_all("SHOW TABLES")
        # MySQL returns dict with unknown key name: Tables_in_<db>
        return [list(r.values())[0] for r in rows]

    def choose_two_tables(self) -> None:
        """Let user choose which two tables are the required application tables."""
        tables = self.list_user_tables()
        if len(tables) < 2:
            raise RuntimeError("Database must contain at least TWO tables for this assignment.")

        print("\nAvailable tables:")
        for i, t in enumerate(tables, start=1):
            print(f"{i}. {t}")

        while True:
            a = input("Choose table # for Table A: ").strip()
            b = input("Choose table # for Table B: ").strip()
            if a.isdigit() and b.isdigit():
                ai = int(a) - 1
                bi = int(b) - 1
                if 0 <= ai < len(tables) and 0 <= bi < len(tables) and ai != bi:
                    self.table_a = tables[ai]
                    self.table_b = tables[bi]
                    print(f"Selected tables: A={self.table_a}, B={self.table_b}")
                    return
            print("Invalid selection. Choose two different table numbers.")

    def clear_tables_before_import(self) -> None:
        """Remove all existing data from both tables before import."""
        self.db.execute(f"DELETE FROM {self.table_a}")
        self.db.execute(f"DELETE FROM {self.table_b}")

    def get_table_columns(self, table_name: str) -> list[str]:
        """Get column names for a table (used to insert only matching fields)."""
        rows = self.db.query_all(f"DESCRIBE {table_name}")
        return [r["Field"] for r in rows]

    def insert_row_into_table(self, table_name: str, row: dict) -> None:
        """
        Insert using only columns that exist in the table.
        ”.
        """
        cols = self.get_table_columns(table_name)

        # Only use keys that exist as columns (skip anything else)
        usable = {k: v for k, v in row.items() if k in cols}

        if not usable:
            return  # nothing to insert (table schema mismatch)

        col_list = ", ".join(usable.keys())
        placeholders = ", ".join(["%s"] * len(usable))
        sql = f"INSERT INTO {table_name} ({col_list}) VALUES ({placeholders})"
        self.db.execute(sql, tuple(usable.values()))

    def load_records_into_tables(self) -> None:
        """Load all in-memory records into both tables."""
        for r in self.records:
            self.insert_row_into_table(self.table_a, r)
            self.insert_row_into_table(self.table_b, r)

    # -------------------------
    # Required menu operations
    # -------------------------
    def import_new_file(self) -> None:
        """Option 1: ask for file, clear tables, import records, export files, load DB."""
        raw_path = input("Enter path to customer_export.txt: ").strip().strip('"')
        file_path = Path(raw_path)

        if not file_path.exists():
            print("File does not exist.")
            return

        try:
            rows = self.parse_export_file(file_path)
            rows = self.dedupe_records(rows)  # attempt remove duplicates
            self.records = rows

            # Remove all existing DB data before importing
            self.clear_tables_before_import()

            # Export JSON/CSV (backup first)
            self.export_phone_json(Path("customer_phone.json"))
            self.export_location_csv(Path("customer_location.csv"))

            # Load into both tables
            self.load_records_into_tables()

            print(f"Imported {len(self.records)} unique records.")
            print("Wrote: customer_phone.json and customer_location.csv")

        except Exception as ex:
            print(f"Import error: {ex}")

    def show_table_data(self) -> None:
        """Option 2: user chooses table, print rows using a loop."""
        table = self._choose_table_prompt()
        try:
            rows = self.db.query_all(f"SELECT * FROM {table}")
            if not rows:
                print("No data found.")
                return

            for r in rows:  # required: print each row using a loop
                print("\n-------------------")
                for k, v in r.items():
                    print(f"{k}: {v}")

        except Exception as ex:
            print(f"Show error: {ex}")

    def add_record(self) -> None:
        """Option 3: Add a record to BOTH tables (validated input)."""
        try:
            new_row = self._prompt_full_record()
            self.insert_row_into_table(self.table_a, new_row)
            self.insert_row_into_table(self.table_b, new_row)
            print("Record added to BOTH tables.")
        except Exception as ex:
            print(f"Add error: {ex}")

    def edit_record(self) -> None:
        """Option 4: Choose table -> choose record -> choose field -> update."""
        table = self._choose_table_prompt()

        try:
            pk = self._choose_primary_key(table)
            if pk is None:
                print("Cannot edit because table has no primary key (or none detected).")
                return

            pk_col, pk_val = pk
            record = self.db.query_one(f"SELECT * FROM {table} WHERE {pk_col}=%s", (pk_val,))
            if not record:
                print("Record not found.")
                return

            print("\nFields:")
            cols = list(record.keys())
            for i, c in enumerate(cols, start=1):
                print(f"{i}. {c}")

            choice = input("Choose field # to edit: ").strip()
            if not choice.isdigit() or not (1 <= int(choice) <= len(cols)):
                print("Invalid field selection.")
                return

            field = cols[int(choice) - 1]
            new_value = input(f"New value for {field}: ")

            # Validate only the fields we know rules for (others pass through)
            validated = self._validate_field(field, new_value)

            # Update ONLY in chosen table (requirement says choose which table to edit)
            self.db.execute(f"UPDATE {table} SET {field}=%s WHERE {pk_col}=%s", (validated, pk_val))
            print("Record updated.")

        except Exception as ex:
            print(f"Edit error: {ex}")

    def delete_record(self) -> None:
        """Option 5: Choose table -> choose record -> confirm -> delete."""
        table = self._choose_table_prompt()

        try:
            pk = self._choose_primary_key(table)
            if pk is None:
                print("Cannot delete because table has no primary key (or none detected).")
                return

            pk_col, pk_val = pk
            record = self.db.query_one(f"SELECT * FROM {table} WHERE {pk_col}=%s", (pk_val,))
            if not record:
                print("Record not found.")
                return

            confirm = input("Type YES to confirm deletion: ").strip().upper()
            if confirm != "YES":
                print("Deletion cancelled.")
                return

            self.db.execute(f"DELETE FROM {table} WHERE {pk_col}=%s", (pk_val,))
            print("Record deleted.")

        except Exception as ex:
            print(f"Delete error: {ex}")

    # -------------------------
    # Internal prompts/helpers
    # -------------------------
    def _choose_table_prompt(self) -> str:
        """Prompt user to choose A or B."""
        if not self.table_a or not self.table_b:
            raise RuntimeError("Tables not selected yet.")
        print(f"\nA = {self.table_a}")
        print(f"B = {self.table_b}")
        choice = input("Choose table (A/B): ").strip().upper()
        return self.table_a if choice == "A" else self.table_b

    def _choose_primary_key(self, table: str):
        """Try to detect PK, then let user pick a record by PK value."""
        # Find primary key column
        rows = self.db.query_all(f"SHOW KEYS FROM {table} WHERE Key_name='PRIMARY'")
        if not rows:
            return None

        pk_col = rows[0]["Column_name"]
        # Show a small list of PK values
        keys = self.db.query_all(f"SELECT {pk_col} FROM {table} ORDER BY {pk_col} LIMIT 25")
        if not keys:
            print("Table is empty.")
            return None

        print(f"\nSelect record by {pk_col}:")
        for r in keys:
            print(f"- {r[pk_col]}")

        pk_val = input(f"Enter {pk_col} value: ").strip()
        return (pk_col, pk_val)

    def _prompt_full_record(self) -> dict:
        """Prompt user for a full record (aligned to rules)."""
        first = validate_name(input("First name: "), "First name")
        last = validate_name(input("Last name: "), "Last name")
        company = validate_company(input("Company name: "))
        address = validate_address(input("Address: "))
        city = validate_city(input("City: "))
        county = validate_county(input("County: "))
        state = validate_state(input("State (2-letter): "))
        zip_code = validate_zip(input("ZIP (4 or 5 digits): "))
        phone1 = validate_phone(input("Phone 1 (blank allowed): "), allow_blank=True)
        phone2 = validate_phone(input("Phone 2 (blank allowed): "), allow_blank=True)
        email = validate_email(input("Email: "))

        # These keys match the export file headers, and are inserted only if columns exist
        return {
            "first_name": first,
            "last_name": last,
            "company_name": company,
            "address": address,
            "city": city,
            "county": county,
            "state": state,
            "zip": zip_code,
            "phone1": phone1 or "",
            "phone2": phone2 or "",
            "email": email
        }

    def _validate_field(self, field: str, value: str):
        """Validate a single field if it matches known fields."""
        f = field.lower()

        if f == "first_name":
            return validate_name(value, "First name")
        if f == "last_name":
            return validate_name(value, "Last name")
        if f == "company_name":
            return validate_company(value)
        if f == "address":
            return validate_address(value)
        if f == "city":
            return validate_city(value)
        if f == "county":
            return validate_county(value)
        if f == "state":
            return validate_state(value)
        if f == "zip":
            return validate_zip(value)
        if f in ("phone1", "phone2"):
            return validate_phone(value, allow_blank=True) or ""
        if f == "email":
            return validate_email(value)

        # Unknown field: accept raw 
        return value.strip()
