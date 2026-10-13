from list_operations import *


def test_create_empty_list():
    assert len(create_list()) == 0

def test_islist_type():
    assert isinstance(create_list(), list)


def test_add_to_list():
    add_to_list("John")
    assert len(create_list()) == 1


def test_get_list_item():
    assert create_list()[0] == 'John'
