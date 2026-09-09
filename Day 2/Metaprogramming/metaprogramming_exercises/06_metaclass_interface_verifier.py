"""
Exercise 6: Metaclass Interface Verifier

Objective:
    Enforce structural layout rules and docstring presence at class
    compilation time.

Instructions:
    Construct a metaclass InterfaceVerifier that ensures any subclass of
    BaseComponent defines a non-empty __doc__ docstring and implements a
    validate() method.

Expected Shell Output:
    DatabaseComponent instantiated successfully.
    Docstring check failed correctly:
    Class 'BrokenDoc' must define a non-empty docstring.
    Method check failed correctly:
    Class 'BrokenMethod' must implement a 'validate(self)' method.
"""

class InterfaceVerifier(type):
    def __new__(mcls, name, bases, namespace):
        # TODO: Enforce structural rules before constructing class
        pass
