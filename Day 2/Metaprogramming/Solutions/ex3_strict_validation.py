"""Exercise 3: Strict Attribute Validation (solution)."""


class StrictEmployee:
    def __init__(self, name, salary):
        self.name = name          # both assignments go through __setattr__
        self.salary = salary

    def __setattr__(self, name, value):
        if name == "name":
            if not isinstance(value, str):
                raise TypeError("Employee name must be a string")
            value = value.strip()                  # normalise
            if not value:
                raise ValueError("Employee name cannot be empty")
        elif name == "salary":
            if not isinstance(value, (int, float)):
                raise TypeError("Salary must be a number")
            if value < 0:
                raise ValueError("Salary cannot be negative")
            value = float(value)                   # normalise
        # self.name = value here would call __setattr__ again forever
        object.__setattr__(self, name, value)


if __name__ == "__main__":
    emp = StrictEmployee("  Alice ", 75000)
    print(f"Employee registered: {emp.name}, salary: {emp.salary}")

    for bad_name, bad_salary in [("   ", 50000), ("Bob", -10), (42, 50000)]:
        try:
            StrictEmployee(bad_name, bad_salary)
        except (TypeError, ValueError) as err:
            print(f"{type(err).__name__}: {err}")
