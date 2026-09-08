# Slide 7: Custom classes can track state across queries

import sqlite3
import time


class QueryTimer:
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        self.start = time.perf_counter()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, tb):
        elapsed = time.perf_counter() - self.start
        print(f'Query took {elapsed:.4f}s')
        self.cursor.close()
        return False


# Usage
if __name__ == "__main__":
    conn = sqlite3.connect('shop.db')
    conn.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER)')
    conn.execute('INSERT INTO orders VALUES (1), (2), (3)')
    conn.commit()

    with QueryTimer(conn) as cur:
        cur.execute('SELECT * FROM orders')
        rows = cur.fetchall()

    print(f"Rows returned: {rows}")
    conn.close()

# Design insight:
# Because the connection is passed in rather than created
# inside, the same QueryTimer wraps any query, anywhere.
