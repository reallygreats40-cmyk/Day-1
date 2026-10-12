# 1. type(obj): which class made this object?
print(type(3.14))                 # <class 'float'>

# 2. type(name, bases, namespace): build a NEW class
def greet(self):
    return f"Hello, I am {self.name}"

Person = type(
    "Person",                           # name of the class
    (),                                 # parents: () means object
    {"name": "Ada", "greet": greet},    # attributes and methods
)

# This is exactly what the class statement does for:
# class Person:
#     name = "Ada"
#     def greet(self): return f"Hello, I am {self.name}"

p = Person()
print(p.greet())                  # Hello, I am Ada
print(Person.__name__)            # Person
