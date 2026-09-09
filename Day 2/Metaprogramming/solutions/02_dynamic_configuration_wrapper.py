"""
Exercise 2: Dynamic Configuration Wrapper - Solution

Objective:
    Turn a dictionary data source into an attribute-based interface using
    __getattr__.

Explanation:
    Overriding __getattr__ intercepts failed attribute lookups and redirects
    them into the internal _data dictionary. If the retrieved value is
    itself a dictionary, it is recursively wrapped in a ReadOnlyConfig
    instance. The custom __setattr__ guards against mutation.
"""

class ReadOnlyConfig:
    def __init__(self, data):
        object.__setattr__(self, "_data", dict(data))

    def __getattr__(self, name):
        if name not in self._data:
            raise AttributeError(f"Attribute '{name}' not found")
        value = self._data[name]
        if isinstance(value, dict):
            return ReadOnlyConfig(value)
        return value

    def __setattr__(self, name, value):
        raise AttributeError("ReadOnlyConfig is immutable.")
