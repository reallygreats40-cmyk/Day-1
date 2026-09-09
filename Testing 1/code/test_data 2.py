from userDB import UsersDatabase
import pytest


@pytest.fixture()
def createResource():
    database = UsersDatabase()
    database.add_user('John', 'Smith', 29, 'e31sf')
    database.add_user('Emily', 'Taylor', 12, 'd24da')
    database.add_user('Lily', 'Thomas', 66, 'd33fw')
    return database


def test_numberOf_users(createResource):
    amount = createResource.get_number_of_users()
    assert amount == 3


def test_duplicate_user(createResource):
    with pytest.raises(ValueError):
        createResource.add_user('John', 'Smith', 29, 'e31sf')


def test_delete_user(createResource):
    createResource.delete_user_by_id("d24da")
    count = createResource.get_number_of_users()
    assert count == 2


def test_string_age_value(createResource):
    with pytest.raises(TypeError):
        createResource.add_user('John', 'Thomas', 'age', 'dc33s')


def test_large_age_value(createResource):
    with pytest.raises(ValueError):
        createResource.add_user('Ava', 'Brown', 200, 'dsd2f')


def test_negative_age_value(createResource):
    with pytest.raises(ValueError):
        createResource.add_user('Ava', 'Brown', -10, 'dsdw3')


def test_numeric_name_value(createResource):
    with pytest.raises(TypeError):
        createResource.add_user(2323, 'Smith', 23, 'd3ff2')


def test_float_surname_value(createResource):
    with pytest.raises(TypeError):
        createResource.add_user('John', 3.14, 19, 'd31xe')


def test_user_without_id(createResource):
    with pytest.raises(TypeError):
        createResource.add_user(name='John', surname='Wilson', age=19)


'''
    For you to do to get 100% coverage
    write a test for get_oldest_user_name()
'''


# a teardown
def test_removeData(createResource):
    createResource.database.clear()
    assert len(createResource.database) == 0


