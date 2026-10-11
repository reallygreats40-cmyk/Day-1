# Exercise 8: Capstone Processing Pipeline Solution
# Task: Stack block timer, temp folder, and sqlite transaction into a pipeline.

import time
import sqlite3
from contextlib import ExitStack, contextmanager
from pathlib import Path
from tempfile import mkdtemp
import shutil

# Local helpers
class Timer:
    def __init__(self):
        self.start = 0.0
        self.elapsed = 0.0
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"[ETL Timer] Process completed in {self.elapsed:.6f} seconds.")

@contextmanager
def temp_workspace():
    raw_path = mkdtemp()
    ws_path = Path(raw_path)
    try:
        yield ws_path
    finally:
        shutil.rmtree(raw_path)

class SQLiteTransaction:
    def __init__(self, db_path):
        self.db_path = db_path
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn
    def __exit__(self, exc_type, exc_val, traceback):
        try:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
        finally:
            self.conn.close()

def run_pipeline(db_path, data):
    with ExitStack() as stack:
        # Stack 1: Timer
        timer = stack.enter_context(Timer())
        # Stack 2: Sandbox working dir
        ws = stack.enter_context(temp_workspace())
        # Stack 3: Transaction
        conn = stack.enter_context(SQLiteTransaction(db_path))

        # Perform pipeline migrations
        conn.execute("CREATE TABLE IF NOT EXISTS migration_users (name TEXT)")
        temp_log = ws / "migration_log.txt"
        temp_log.write_text(f"Starting migration of {len(data)} records.\n")

        for row in data:
            conn.execute("INSERT INTO migration_users (name) VALUES (?)", row)
            time.sleep(0.05) # Simulate database I/O latency

        temp_log.write_text(f"Migration completed successfully.\n")
        print("[Pipeline] Temporary log contains:", temp_log.read_text().strip())

# Verification
if __name__ == "__main__":
    run_pipeline(":memory:", [("Alice",), ("Bob",), ("Charlie",)])
