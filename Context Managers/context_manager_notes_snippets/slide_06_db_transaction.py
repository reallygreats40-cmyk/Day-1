# Slide 6: Database transactions demand error-aware safety

import sqlite3
from contextlib import contextmanager


@contextmanager
def db_transaction(path):
    conn = sqlite3.connect(path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()  # no connection leaks


# Usage
if __name__ == "__main__":
    # Set up a table to work with
    setup_conn = sqlite3.connect('shop.db')
    setup_conn.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER)')
    setup_conn.commit()
    setup_conn.close()

    with db_transaction('shop.db') as conn:
        conn.execute('INSERT INTO orders VALUES (?)', (42,))

    # Confirm the row was committed
    check_conn = sqlite3.connect('shop.db')
    rows = check_conn.execute('SELECT * FROM orders').fetchall()
    print(f"Orders table now contains: {rows}")
    check_conn.close()

# Design insight:
# conn.commit() sits inside the try, right after yield, so
# it only runs when the caller's block completes cleanly.
