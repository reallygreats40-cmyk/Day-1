# Exercise 3: SQLite Transaction Manager Solution
# Task: Build a class-based database context manager named SQLiteTransaction.

import sqlite3

class SQLiteTransaction:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def __exit__(self, exc_type, exc_val, traceback):
        try:
            if exc_type is None:
                self.conn.commit()
                print("[Database] Commit complete.")
            else:
                self.conn.rollback()
                print(f"[Database] Rollback triggered due to error: {exc_val}")
        finally:
            self.conn.close()
        return False # Let exceptions propagate

# Verification
if __name__ == "__main__":
    with SQLiteTransaction(":memory:") as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("INSERT INTO users (name) VALUES ('Alice')")
        
        # Test rollback on exception
        try:
            with SQLiteTransaction(":memory:") as conn2:
                conn2.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
                conn2.execute("INSERT INTO users (name) VALUES ('Bob')")
                raise ValueError("Simulated DB failure")
        except ValueError as e:
            print("Caught expected rollback error:", e)
