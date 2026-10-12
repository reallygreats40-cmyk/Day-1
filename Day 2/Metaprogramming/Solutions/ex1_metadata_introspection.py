"""Exercise 1: Dynamic Metadata Introspection (solution)."""


def inspect_class(cls):
    """Return a summary dictionary describing any class."""
    attributes = [
        attr for attr in cls.__dict__      # only names defined in this class
        if not attr.startswith("__")       # skip Python's own dunder names
    ]
    return {
        "name": cls.__name__,
        "bases": [base.__name__ for base in cls.__bases__],
        "mro": [klass.__name__ for klass in cls.__mro__],
        "attributes": attributes,
    }


if __name__ == "__main__":
    class Parent:
        category = "base"

    class Child(Parent):
        value = 100

        def run(self):
            pass

    meta = inspect_class(Child)
    print("Class name:", meta["name"])
    print("Bases:", meta["bases"])
    print("MRO:", meta["mro"])
    print("Own attributes:", sorted(meta["attributes"]))
