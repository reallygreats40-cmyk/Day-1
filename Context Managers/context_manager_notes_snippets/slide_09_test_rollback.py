# Slide 9: Test both the success and the failure path

import sqlite3
from contextlib import contextmanager


@contextmanager
def db_transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

def test_rollback_on_error():
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE t (id INTEGER)')
    try:
        with db_transaction(conn):
            conn.execute('INSERT INTO t VALUES (1)')
            raise ValueError('simulated failure')
    except ValueError:
        pass
    count = conn.execute('SELECT COUNT(*) FROM t').fetchone()[0]
    assert count == 0  # rollback verified


def test_commit_on_success():
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE t (id INTEGER)')
    with db_transaction(conn):
        conn.execute('INSERT INTO t VALUES (1)')
    count = conn.execute('SELECT COUNT(*) FROM t').fetchone()[0]
    assert count == 1  # commit verified


if __name__ == "__main__":
    test_rollback_on_error()
    print("Rollback verified: table is empty")
    test_commit_on_success()
    print("Commit verified: row was saved")

# Design insight:
# Because SQLite can run entirely in memory, the test stays
# fast while still exercising the real commit/rollback code.
