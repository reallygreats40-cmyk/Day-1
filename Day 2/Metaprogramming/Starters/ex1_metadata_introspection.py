"""Exercise 1: Dynamic Metadata Introspection (starter).

Complete inspect_class(cls) so that it returns a dictionary with:
  "name"       the class name, e.g. "Child"
  "bases"      names of the direct parent classes, e.g. ["Parent"]
  "mro"        names of every class in the MRO, e.g. ["Child", "Parent", "object"]
  "attributes" names defined in the class itself, excluding dunder names

Hints: cls.__name__, cls.__bases__, cls.__mro__, cls.__dict__
"""


def inspect_class(cls):
    """Return a summary dictionary describing any class."""
    # TODO: build and return the dictionary described above
    pass


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
