"""Exercise 2: Dynamic Configuration Wrapper (starter).

Complete __getattr__ so that config.debug reads the "debug" key, nested
dictionaries can be read with dots (config.database.host), and a missing
key raises AttributeError.

Hints:
  - __getattr__ runs only when normal attribute lookup fails.
  - Raise AttributeError straight away for names starting with "_";
    otherwise reading self._data before it exists would call
    __getattr__ again, forever.
  - Wrap a nested dict in a new ReadOnlyConfig before returning it.
"""


class ReadOnlyConfig:
    def __init__(self, data):
        # Our own __setattr__ blocks writes, so store _data directly
        object.__setattr__(self, "_data", dict(data))

    def __getattr__(self, name):
        # TODO: look up name in self._data as described above
        pass

    def __setattr__(self, name, value):
        raise AttributeError("ReadOnlyConfig is read-only.")


if __name__ == "__main__":
    config = ReadOnlyConfig({
        "debug": True,
        "database": {"host": "localhost", "port": 5432},
    })
    print("Debug:", config.debug)
    print("Database host:", config.database.host)
    print("Database port:", config.database.port)

    try:
        config.timeout
    except AttributeError as err:
        print("Missing key:", err)

    try:
        config.debug = False
    except AttributeError as err:
        print("Write blocked:", err)
