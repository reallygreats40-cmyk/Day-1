import pytest

from usersDB import UsersDatabase

def test_user_database():
    # Create user database object
    database = UsersDatabase()

    # Add new users
    database.add_user('John', 'Smith', 29, 'e31sf')
    database.add_user('Emily', 'Taylor', 12, 'd24da')
    database.add_user('Lily', 'Thomas', 66, 'd33fw')
    assert database.get_number_of_users() == 3

    # Add two users with the same id
    with pytest.raises(ValueError):
        database.add_user('John', 'Smith', 29, 'e31sf')

    # Remove user
    database.delete_user_by_id('d24da')
    assert database.get_number_of_users() == 2

    # What if age is a string
    with pytest.raises(TypeError):
        database.add_user('John', 'Thomas', 'age', 'dc33s')

    # What if age equals 200
    with pytest.raises(ValueError):
        database.add_user('Ava', 'Brown', 200, 'dsd2f')

    # What if age is negative value
    with pytest.raises(ValueError):
        database.add_user('Ava', 'Brown', -10, 'dsdw3')

    # What if name is a integer
    with pytest.raises(TypeError):
        database.add_user(2323, 'Smith', 23, 'd3ff2')

    # What if surname is a float
    with pytest.raises(TypeError):
        database.add_user('John', 3.14, 19, 'd31xe')

    # What if new user doesn't have id
    with pytest.raises(TypeError):
        database.add_user(name='John', surname='Wilson', age=19)
