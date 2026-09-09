"""
Dynamic Classes: constructing classes with type()
====================================================

WHAT THIS SHOWS
----------------
'type' has two completely different jobs depending on how many arguments
you give it:

  1. type(some_object)              -> reports the class of some_object.
  2. type(name, bases, namespace)   -> BUILDS a brand new class.

The three-argument form is exactly what the `class` statement compiles
down to behind the scenes. Writing:

    class Person:
        name = "Ada"
        def greet(self): ...

is just a more readable way of writing:

    Person = type("Person", (), {"name": "Ada", "greet": greet})

WHY THIS MATTERS
----------------
The `class` keyword requires the shape of the class, its name, its
attributes, its methods, to be known and typed out in your source code.
type() lets you build that same kind of object when the shape is only
known while the program is RUNNING: read from a database, a config file,
a schema definition, or generated in a loop.

WHERE THIS SHOWS UP IN REAL CODE
---------------------------------
- ORMs generating a model class on the fly from a database table's
  column definitions, instead of requiring a hand-written class per
  table.
- Building lightweight test doubles or mock classes inside a test suite,
  where the exact attributes needed vary test to test.
- Libraries like `collections.namedtuple` and
  `dataclasses.make_dataclass`, which are themselves thin wrappers
  around dynamic class construction.
- Turning a JSON Schema, OpenAPI spec, or plugin manifest into real
  Python classes without writing one class per entry by hand.

A GUIDING RULE FROM THE NOTES
------------------------------
Prefer a normal, static `class` definition whenever the structure is
already known while you are writing the code. Reach for type() only when
the structure genuinely cannot be known until runtime.
"""


def greet(self):
    # An ordinary function, defined completely separately from any
    # class. Because its first parameter is named `self`, it can later
    # be attached to a class and used exactly like a normal method.
    return f"Hello, I am {self.name}"


# Dynamic class construction with the 3-argument form of type():
#   type(name, bases, namespace)
Person = type(
    "Person",
    # bases: a TUPLE of parent classes for the new class to inherit
    # from. An empty tuple, (), means "no explicit parent", which is
    # exactly what `class Person:` (with no parentheses) also means:
    # Person still inherits from `object`, Python's default base for
    # every class, just implicitly.
    (),
    # namespace: a dict of the class's attributes and methods, exactly
    # as if they had been written inside a `class Person:` body.
    {"name": "Ada", "greet": greet},
)


if __name__ == "__main__":
    p = Person()
    print(p.greet())        # 'Hello, I am Ada'
    print(Person.__name__)  # 'Person'

    # Because Person was built with the plain three-argument type() call,
    # it behaves completely normally: it can be subclassed, instantiated
    # many times, and introspected exactly like any hand-written class.
    print(isinstance(p, Person))       # True
    print(type(Person) is type)        # True: Person's own metaclass is
                                        # the default, plain `type`.
