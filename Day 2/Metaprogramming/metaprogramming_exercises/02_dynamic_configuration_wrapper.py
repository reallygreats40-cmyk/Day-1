"""
Exercise 2: Dynamic Configuration Wrapper

Objective:
    Turn a dictionary data source into an attribute-based interface using
    __getattr__.

Instructions:
    Create a ReadOnlyConfig class that takes a dictionary and permits
    accessing nested keys via dot notation, raising AttributeError for
    missing attributes.

Expected Shell Output:
    Debug state: True
    DB Host: localhost
"""

class ReadOnlyConfig:
    def __init__(self, data):
        object.__setattr__(self, "_data", dict(data))

    def __getattr__(self, name):
        # TODO: Implement dynamic lookup and wrap nested dicts
        pass

    def __setattr__(self, name, value):
        raise AttributeError("ReadOnlyConfig is immutable.")
