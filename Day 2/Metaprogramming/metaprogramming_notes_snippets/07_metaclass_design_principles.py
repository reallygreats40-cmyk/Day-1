"""
Design Principles: using metaclasses sparingly
==================================================

WHAT THIS SHOWS
----------------
Metaclasses are one of the most powerful tools in Python, and one of the
least readable. This slide is a set of guiding principles for using them
well, rather than a new technique on its own.

MetaBase, below, is a minimal example: a metaclass that stamps every
class built with it with a "meta_tag" attribute, by modifying the raw
namespace dict BEFORE the class object exists. That "before the class
exists" timing is the one thing only a metaclass can do.

WHY THIS MATTERS
----------------
This is the "Rule of Least Power" in practice: always reach for the
simplest mechanism that solves the actual problem. Prefer an ordinary
class, a simple class decorator, or a plain validation function first.
Reach for a custom metaclass only when the class CREATION process itself
must be controlled, for example, altering what arguments the `class`
statement accepts, or needing to inspect and modify the namespace before
the class exists at all.

WHERE THIS MATTERS IN REAL CODE
----------------------------------
- Most validation, registration, and "remember every subclass" needs are
  simple problems that do not require this level of power.
- Reach for a metaclass when: the class needs to work even for code that
  does not inherit from a shared base you control, or you need to alter
  the class BEFORE it exists (e.g. auto-generating __slots__, renaming
  attributes, or rejecting a malformed class body outright), or you are
  building infrastructure-level tooling like an ORM base class, similar
  to Django's or SQLAlchemy's.
- A practical risk: two unrelated libraries each supplying their OWN
  metaclass for the same class can conflict with each other in ways that
  are hard to resolve. Keeping metaclass logic small, isolated, and well
  documented limits how often this happens.
"""


class MetaBase(type):
    def __new__(mcls, name, bases, d):
        # Modifies the raw namespace dict before the class exists.
        # `d` is the class body's namespace, still just a plain dict at
        # this point, not yet a class. Adding a key here means every
        # class built with this metaclass gets "meta_tag" for free,
        # without writing it in each class body.
        d["meta_tag"] = True
        return type.__new__(mcls, name, bases, d)


if __name__ == "__main__":
    class Widget(metaclass=MetaBase):
        pass

    print("Widget.meta_tag:", Widget.meta_tag)  # True
    # Every class built with MetaBase gets this automatically, without
    # ever writing `meta_tag = True` inside the class body itself.
