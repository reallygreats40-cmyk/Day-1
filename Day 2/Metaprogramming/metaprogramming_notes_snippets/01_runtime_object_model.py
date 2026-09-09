"""
Runtime Object Model: classes and objects are runtime values
==============================================================

WHAT THIS SHOWS
----------------
In Python, a class is not a compile-time-only blueprint the way it is in
some statically typed languages. A class is itself a full, first-class
object that exists while the program is running. That means a class can
be passed to a function, stored in a variable, put in a list, or built
on the fly, exactly like a string, an integer, or any other value.

Every object also carries a live, inspectable link back to the class
that built it, and every class exposes its own ancestry: which classes
it inherits from ('__bases__'), and the full, ordered chain Python will
search when looking up an attribute ('__mro__', the Method Resolution
Order).

WHY THIS MATTERS
----------------
This introspection is not a party trick. It is the foundation that every
other metaprogramming technique in this collection is built on top of:
before you can dynamically validate, register, or generate a class, your
code first has to be able to ASK questions about classes at runtime
("what type is this?", "what does it inherit from?", "does it already
define this method?"). Without runtime visibility into classes, none of
that would be possible.

WHERE THIS SHOWS UP IN REAL CODE
---------------------------------
- Serialization libraries (e.g. turning an object into JSON) look at
  '__class__' and its attributes to decide how to represent an object.
- Debuggers, loggers, and pretty-printers use '__class__.__name__' to
  produce readable output like "<Account object>" instead of a raw
  memory address.
- Testing frameworks implement assertIsInstance() and similar checks by
  walking '__mro__' to see if a class appears anywhere in an object's
  inheritance chain.
- Object-relational mappers (ORMs) inspect a model class's bases and
  attributes to work out which database table and columns it maps to.
- The 'pickle' and 'copy' modules rely on '__class__' to know how to
  reconstruct an object.
"""


class Account:
    pass


account = Account()

# __class__ is a live reference from the INSTANCE back to the class that
# constructed it. It answers "what kind of thing is this, right now?"
print(account.__class__)
# Outputs: <class '__main__.Account'>

# __name__ is a plain string: just the class's own name, no module path.
# Useful anywhere you want a human-readable label (logs, error messages).
print(Account.__name__)
# Outputs: 'Account'

# __bases__ is a tuple of the classes THIS class directly inherits from.
# Account didn't declare a parent explicitly, so Python gave it the
# implicit default: object, the ancestor of every class in Python.
print(Account.__bases__)
# Outputs: (<class 'object'>,)

# __mro__ (Method Resolution Order) is the FULL search order Python will
# walk through when looking up an attribute or method on this class,
# including indirect ancestors. For a simple single-inheritance class
# like this, it is just Account itself, then object.
print(Account.__mro__)
# Outputs: (<class '__main__.Account'>, <class 'object'>)


if __name__ == "__main__":
    # A tiny extra demonstration: introspection lets you write code that
    # reacts to WHAT a class is, without hardcoding its name anywhere.
    def describe(obj):
        cls = obj.__class__
        parents = ", ".join(base.__name__ for base in cls.__bases__)
        print(f"{cls.__name__} instance, inherits from: {parents}")

    describe(account)
