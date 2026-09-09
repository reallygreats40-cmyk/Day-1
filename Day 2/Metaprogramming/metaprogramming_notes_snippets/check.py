class Example:
    def __init__(self):
        self.x = 10  # sets x in instance __dict__

    def __getattr__(self, name):
        print(f"__getattr__ called for {name}")
        return "default"

f = Example()
print(f.x)   # 10 — found in __dict__, __getattr__ never runs
print(f.y)   # __getattr__ called for y -> "default"


# only compute or fetch something when it's actually requested, rather than in __init__
class Report:
    def __init__(self, data_source):
        self.data_source = data_source

    def __getattr__(self, name):
        if name == "summary":
            print("Computing summary...")
            self.summary = 'expensive_computation(self.data_source)'
            return self.summary
        raise AttributeError(name)


 # good use of setattr and getattr
class Person:
    def __init__(self, age):
        self._validate(age)
        object.__setattr__(self, "_age", age)

    def _validate(self, age):
        if not isinstance(age, int):
            raise TypeError("age must be an int")
        if age < 0:
            raise ValueError("age cannot be negative")

    def __getattr__(self, name):
        if name == "age":
            return self._age
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == "age":
            raise AttributeError("age is read-only")
        super().__setattr__(name, value)


'''
p = Person(30)
print(p.age)     # 30
p.age = 40        # AttributeError: age is read-only
Person(-5)        # ValueError
Person("30")      # TypeError
'''