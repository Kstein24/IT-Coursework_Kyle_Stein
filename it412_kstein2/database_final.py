# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

"""
database.py

Small database helper class using PyMySQL (XAMPP MySQL port 3307).
Parameter queries are used so quotes in text won't break SQL.
"""

import pymysql


class Database:
    """Simple DB wrapper for SELECT/INSERT/UPDATE/DELETE."""

    def __init__(self, host="127.0.0.1", user="root", password="", database="", port=3307):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = None

    def connect(self):
        """Open a connection if not already opened."""
        if self.conn is None:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )

    def close(self):
        """Close connection."""
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def query_all(self, sql, params=None):
        """Run SELECT returning many rows."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.fetchall()

    def query_one(self, sql, params=None):
        """Run SELECT returning one row or None."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.fetchone()

    def execute(self, sql, params=None):
        """Run INSERT/UPDATE/DELETE and return affected count."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.rowcount
