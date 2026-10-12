"""Exercise 4: Generating a Class with type() (starter).

Complete class_factory(class_name, fields) so that it returns a NEW class:
  - its __init__ takes one value per field, in order, and stores each
    one (raise TypeError if the number of values is wrong);
  - its __repr__ shows the values, e.g. Point3D(x=10, y=20, z=30).

Hint: define the two functions inside class_factory, put them in a
namespace dictionary, then call type(class_name, (), namespace).
"""


def class_factory(class_name, fields):
    """Build a new class whose __init__ sets the given fields in order."""
    # TODO: define __init__ and __repr__, then build the class with type()
    pass


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
