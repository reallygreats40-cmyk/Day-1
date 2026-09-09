"""
Metaprogramming Core: coordinating class creation with metaclasses
=======================================================================

WHAT THIS SHOWS
----------------
A metaclass is, quite literally, "a class of a class": the thing that
builds a class, the same way an ordinary class builds instances. By
default, every class in Python is built by the same metaclass, `type`.
Subclassing `type` and overriding its `__new__` lets you intercept and
even change a class's raw namespace dict BEFORE the class object is
finished being constructed, something no other hook in Python can do.

Here, RequireRun checks, at the moment ANY class using it as a metaclass
is being built, whether that class's namespace dict already contains a
"run" key. If not (and it is not the special "Base" class itself, which
is allowed to be abstract), class construction is aborted with a
TypeError before the class ever comes into existence.

WHY THIS MATTERS
----------------
This enforces a contract at IMPORT time, the moment Python reads and
executes the class definition, rather than waiting until someone tries
to call .run() on an instance and gets a plain AttributeError far away
from the actual mistake. It is a stronger, earlier guarantee than
duck-typing or a runtime hasattr() check could give you.

WHERE THIS SHOWS UP IN REAL CODE
---------------------------------
- Django's model metaclass processes each model class's fields and
  Meta options at class-creation time to build the database mapping.
- SQLAlchemy's declarative base uses a metaclass to turn class
  attributes into table columns.
- Python's own `abc.ABCMeta` (which powers abstract base classes) is
  implemented exactly this way: a metaclass that can refuse to let an
  incomplete class be instantiated.
- `enum.EnumMeta` is what makes `class Color(Enum): RED = 1` behave so
  differently from an ordinary class.

A CAUTION FROM THE NOTES
--------------------------
Metaclass logic should stay small, isolated, and documented. It is a
powerful tool, but also one of the least readable in Python, and it is
easy to accidentally make an entire class hierarchy harder to understand
for a modest amount of validation.
"""


class RequireRun(type):
    def __new__(mcls, name, bases, namespace):
        # This runs for EVERY class built with metaclass=RequireRun,
        # including Base itself. `namespace` is the raw dict of
        # everything defined in the class body, before the class object
        # exists.
        if name != "Base" and "run" not in namespace:
            # Base is allowed to be "abstract" (no run() of its own);
            # every other class using this metaclass must define one.
            raise TypeError(f"{name} must define run()")

        # Let the real class-construction machinery (type.__new__) do
        # the actual work of building the class object, now that the
        # check has passed.
        return super().__new__(mcls, name, bases, namespace)


class Base(metaclass=RequireRun):
    # Base has no run() of its own, which is fine: it is explicitly
    # exempted by the `name != "Base"` check above.
    pass


class Job(Base):
    # Job inherits RequireRun automatically, since metaclasses are
    # inherited just like anything else. Its namespace DOES contain
    # "run", so construction succeeds.
    def run(self):
        return "ok"


if __name__ == "__main__":
    j = Job()
    print(j.run())  # 'ok'

    # Uncommenting this class definition raises TypeError the moment
    # Python tries to build it, before a single BrokenJob is ever
    # instantiated:
    #
    # class BrokenJob(Base):
    #     pass
    #
    try:
        class BrokenJob(Base):
            pass
    except TypeError as e:
        print("TypeError raised correctly:", e)
