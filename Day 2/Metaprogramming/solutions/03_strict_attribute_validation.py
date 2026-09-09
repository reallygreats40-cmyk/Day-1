"""
Exercise 3: Strict Attribute Validation - Solution

Objective:
    Intercept attribute assignment to validate or normalise values.

Explanation:
    Overriding __setattr__ intercepts attribute writes. To avoid infinite
    recursion, the actual write is delegated to object.__setattr__(self,
    name, value). Type and value checks run before the write is committed.
"""

class StrictEmployee:
    def __setattr__(self, name, value):
        if name == "name":
            if not isinstance(value, str):
                raise TypeError("Employee name must be of type 'str'")
            if len(value.strip()) == 0:
                raise ValueError("Employee name cannot be empty")
        elif name == "salary":
            if not isinstance(value, (int, float)):
                raise TypeError("Salary must be a numeric value")
            if value < 0:
                raise ValueError("Salary cannot be negative")
        object.__setattr__(self, name, value)
