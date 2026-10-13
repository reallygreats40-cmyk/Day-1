import os
import pytest
import sqlite3


@pytest.fixture()
def db():
    conn = sqlite3.connect('abc')
    # cursor = conn.cursor()
    conn.execute('CREATE TABLE if not exists stock '
                 '(name TEXT, price float)')
    return conn


# setup
@pytest.fixture()
def test_sqlite(db):
    db.execute('INSERT INTO stock (name, price) VALUES ("car", 2000)')


# test 1
# @pytest.mark.skip
# @pytest.mark.skip(reason="cannot testing this for now")
def test_select_data(db, test_sqlite):
    c = db.execute('SELECT * FROM stock;')
    assert list(c) == [('car', 2000)]

    # test ...

    # test N


def test_select_where(db, test_sqlite):
    c = db.execute('SELECT * FROM stock WHERE name = "car";')
    # pytest.skip("not possible with d xyz")
    assert list(c) == [('car', 2000)]


@pytest.fixture()
def tearDown(db):
    db.close()
    os.remove('abc')


def test_db_removed(db, tearDown):
    pass
    #c = db.execute('SELECT * FROM stock WHERE name = "car";')
    # pytest.skip("not possible with d xyz")
    #assert list(c) == []
