class RequireRun(type):
    """A metaclass: it controls how CLASSES are created."""

    def __new__(mcls, name, bases, namespace):
        # Runs when a class statement is executed,
        # before the new class object exists
        if bases and "run" not in namespace:
            raise TypeError(f"{name} must define run()")
        return super().__new__(mcls, name, bases, namespace)

class Base(metaclass=RequireRun):   # no parents: allowed
    pass

class Job(Base):                    # defines run(): allowed
    def run(self):
        return "ok"

try:
    class BrokenJob(Base):          # no run(): rejected at once
        pass
except TypeError as err:
    print(err)                      # BrokenJob must define run()

print(type(Job))                    # <class '__main__.RequireRun'>
