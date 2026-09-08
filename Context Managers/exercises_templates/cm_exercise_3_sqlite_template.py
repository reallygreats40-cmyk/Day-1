# Exercise 3: SQLite Transaction Manager Template
# Task: Build a class-based database context manager named SQLiteTransaction.

import sqlite3

class SQLiteTransaction:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        # TODO: Connect to SQLite database, return connection handle
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        # TODO: Commit on success, rollback on exception, close connection
        pass

# Verification Code
if __name__ == "__main__":
    with SQLiteTransaction(":memory:") as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("INSERT INTO users (name) VALUES ('Alice')")
