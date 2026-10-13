# Kyle Stein 
# Walsh College
# IT 412
# 2/6/2026
# Week 6 & 7 Python Database

"""
database.py

Database wrapper using PyMySQL.
Use parameterized SQL to safely handle quotes (like ' and ") in titles.
"""

import pymysql


class Database:
    """Basic Database class for running queries safely."""

    def __init__(self, host="localhost", user="root", password="", database="bookstore_db", port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = None

    def connect(self):
        """Open a connection if needed."""
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
        """Run a SELECT returning many rows."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.fetchall()

    def query_one(self, sql, params=None):
        """Run a SELECT returning one row or None."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.fetchone()

    def execute(self, sql, params=None):
        """Run INSERT/UPDATE/DELETE and return affected row count."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.rowcount
