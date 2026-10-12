"""Exercise 4: Generating a Class with type() (solution)."""


def class_factory(class_name, fields):
    """Build a new class whose __init__ sets the given fields in order."""

    def __init__(self, *args):
        if len(args) != len(fields):
            raise TypeError(
                f"{class_name} expects {len(fields)} values, got {len(args)}")
        for field, value in zip(fields, args):
            setattr(self, field, value)

    def __repr__(self):
        values = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
        return f"{class_name}({values})"

    namespace = {"__init__": __init__, "__repr__": __repr__}
    return type(class_name, (), namespace)    # name, parents, namespace


if __name__ == "__main__":
    Point3D = class_factory("Point3D", ["x", "y", "z"])
    p = Point3D(10, 20, 30)
    print("Class name:", Point3D.__name__)
    print("Coordinates:", p.x, p.y, p.z)
    print("Object:", p)

    try:
        Point3D(1, 2)
    except TypeError as err:
        print("Error:", err)
