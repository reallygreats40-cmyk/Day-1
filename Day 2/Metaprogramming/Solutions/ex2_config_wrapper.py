"""Exercise 2: Dynamic Configuration Wrapper (solution)."""


class ReadOnlyConfig:
    def __init__(self, data):
        # Our own __setattr__ blocks writes, so store _data directly
        object.__setattr__(self, "_data", dict(data))

    def __getattr__(self, name):
        # Called only when normal lookup fails.
        # Private names are never config keys; refusing them here also
        # prevents endless recursion if _data does not exist yet
        # (for example while the object is being copied).
        if name.startswith("_"):
            raise AttributeError(name)
        if name not in self._data:
            raise AttributeError(f"No setting called '{name}'")
        value = self._data[name]
        if isinstance(value, dict):
            return ReadOnlyConfig(value)    # wrap nested sections too
        return value

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
