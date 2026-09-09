"""
Exercise 1: Dynamic Metadata Introspection - Solution

Objective:
    Access dunder attributes like __name__, __bases__, __mro__, and __dict__
    to audit class structure dynamically.

Explanation:
    This exercise reviews dynamic introspection. Accessing cls.__name__,
    cls.__bases__, and cls.__mro__ retrieves essential runtime hierarchies.
    Filtering cls.__dict__ with a simple list comprehension screens out
    standard dunder namespace attributes.
"""

def inspect_class(cls):
    name = cls.__name__
    bases = cls.__bases__
    mro = cls.__mro__
    attributes = [
        attr for attr in cls.__dict__
        if not attr.startswith("__")
    ]
    return {
        "name": name,
        "bases": bases,
        "mro": mro,
        "attributes": attributes
    }


# Verification Code
class Parent:
    category = "base"

class Child(Parent):
    value = 100
    def run(self): pass

meta = inspect_class(Child)
print("Class Name:", meta.get("name"))
print("User Attributes:", sorted(meta.get("attributes", [])))
