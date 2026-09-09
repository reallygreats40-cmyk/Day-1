"""
Exercise 4: Generating a Class with type() - Solution

Objective:
    Dynamically create custom class architectures programmatically.

Explanation:
    This demonstrates programmatic class creation. A custom __init__
    function binds arguments to instance fields, is placed in a namespace
    dictionary, and is passed to type(name, bases, namespace) to produce a
    new, dynamic class.
"""

def class_factory(class_name, fields):
    def __init__(self, *args):
        if len(args) != len(fields):
            raise TypeError("Argument count mismatch")
        for field, value in zip(fields, args):
            setattr(self, field, value)

    namespace = {"__init__": __init__}
    return type(class_name, (), namespace)
