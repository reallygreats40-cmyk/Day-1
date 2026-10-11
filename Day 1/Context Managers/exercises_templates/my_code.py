'''
relating classes - 1-1, 1- m
inheritance

overloaded methods, injecting data at runtime / reflection

'''

# object
class Car:
    def __init__(self, model): # constructor, initialiser
        self.model = model
        self.price = 0

    def get_model(self):
        return self.model

    def __str__(self):
        return self.model

class Person:
    def __init__(self, fullname):
        self.fullname = fullname
        self.car_list = []

    def get_name(self):
        return self.fullname

    def get_car(self, i):
        return self.car_list[i]

    def count_cars(self):
        return len(self.car_list)

    def add_car(self, car):
        self.car_list.append(car)

# p --> c
# Turing
person = Person('Ada Lovelace')
mycar = Car('Toyota')
person.add_car(mycar)
print(person.get_car(0))
print(f'{person.get_name()} has {person.count_cars()}')
# mycar = Car('Toyota')
# mycar2 = Car('Jaguar')
#
# cars = [mycar2, mycar]
# for i in cars:
#     print(i.get_model())