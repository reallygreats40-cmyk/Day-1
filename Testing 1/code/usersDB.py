
class UsersDatabase:
    def __init__(self):
        self.database = []

    def add_user(self, name, surname, age, id_number):
        if not isinstance(age, int):
            raise TypeError

        if not isinstance(name, str):
            raise TypeError

        if not isinstance(surname, str):
            raise TypeError

        if age not in range(1, 120):
            raise ValueError

        if any(user.id_number == id_number for user in self.database):
            raise ValueError

        self.database.append(User(name, surname, age, id_number))

    def delete_user_by_id(self, id_number):
        for user in self.database:
            if user.id_number == id_number:
                self.database.remove(user)

    def get_oldest_user_name(self):
        oldest_user = sorted(self.database, key=lambda x: x.age, reverse=True)[0]
        return oldest_user.name

    def get_number_of_users(self):
        return len(self.database)


class User:
    def __init__(self, name, surname, age, id_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.id_number = id_number
