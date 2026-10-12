"""Exercise 3: Strict Attribute Validation (starter).

Complete __setattr__ so that:
  - name must be a string (TypeError) and not empty after stripping
    spaces (ValueError); store the stripped name.
  - salary must be an int or float (TypeError) and not negative
    (ValueError); store it as a float.
  - the value is finally stored with object.__setattr__(self, name, value)

Note: __init__ is already written; its assignments pass through __setattr__.
"""


class StrictEmployee:
    def __init__(self, name, salary):
        self.name = name          # both assignments go through __setattr__
        self.salary = salary

    def __setattr__(self, name, value):
        # TODO: validate and normalise, then store with object.__setattr__
        pass


if __name__ == "__main__":
    emp = StrictEmployee("  Alice ", 75000)
    print(f"Employee registered: {emp.name}, salary: {emp.salary}")

    for bad_name, bad_salary in [("   ", 50000), ("Bob", -10), (42, 50000)]:
        try:
            StrictEmployee(bad_name, bad_salary)
        except (TypeError, ValueError) as err:
            print(f"{type(err).__name__}: {err}")
