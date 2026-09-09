"""
Exercise 3: Strict Attribute Validation

Objective:
    Intercept attribute assignment to validate or normalise values.

Instructions:
    Build a StrictEmployee class that checks that 'salary' cannot be
    negative, and 'name' must be a non-empty string, raising TypeError or
    ValueError as appropriate.

Expected Shell Output:
    Employee registered: Alice, Salary: 75000.0
    Pristine name validation error: Employee name cannot be empty
    Pristine salary validation error: Salary cannot be negative
"""

class StrictEmployee:
    def __setattr__(self, name, value):
        # TODO: Add validations and delegate assignment using object.__setattr__
        pass
