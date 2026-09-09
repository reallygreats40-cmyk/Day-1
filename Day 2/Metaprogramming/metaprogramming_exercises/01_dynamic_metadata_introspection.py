"""
Exercise 1: Dynamic Metadata Introspection

Objective:
    Access dunder attributes like __name__, __bases__, __mro__, and __dict__
    to audit class structure dynamically.

Instructions:
    Write a function inspect_class(cls) that returns a summary dictionary of
    metadata for any class.

Expected Shell Output:
    Class Name: Child
    User Attributes: ['run', 'value']
"""

def inspect_class(cls):
    """
    Returns a dictionary with keys:
    'name', 'bases', 'mro', and 'attributes'.
    """
    # TODO: Populate and return the metadata summary dictionary
    pass


# Verification Code
class Parent:
    category = "base"

class Child(Parent):
    value = 100
    def run(self): pass

meta = inspect_class(Child)
print("Class Name:", meta.get("name"))
print("User Attributes:", sorted(meta.get("attributes", [])))
