"""
Namespace Control: customizing attribute assignment with __setattr__
========================================================================

WHAT THIS SHOWS
----------------
Unlike '__getattr__', which only runs on a failed READ, '__setattr__'
intercepts EVERY single attribute assignment on an instance, no
exceptions, whether the attribute already exists or not. That makes it
the natural place to put validation or normalization logic that must run
no matter how or when a value is set.

WHY THIS MATTERS
----------------
Because '__setattr__' intercepts EVERY assignment, writing the "obvious"
self.name = value INSIDE __setattr__ would itself be caught by the same
override: that line is an assignment, so Python routes it straight back
into __setattr__ again, which contains the same self.name = value line,
which is routed back in again, and so on, forever. This is the recursive
loop the notes warn about.

The fix is to bypass the override for the actual write, by calling
object.__setattr__(self, name, value) directly. This calls Python's
default, built-in attribute-assignment logic instead of this class's own
__setattr__, so the value is stored on the instance without triggering
the override again.

WHERE THIS SHOWS UP IN REAL CODE
---------------------------------
- Validating invariants at the moment they would be broken (e.g. an age,
  price, or quantity that must never go negative), rather than
  discovering the bad value much later when something else crashes.
- "Dirty tracking" in an ORM: recording that a field changed so the
  framework knows to include it in the next database UPDATE.
- Read-only or frozen objects: raising an error on any attempt to set an
  attribute after construction.
- Keeping a cache, a UI widget, or a log file in sync automatically
  whenever a particular field changes (write-through / observer style
  patterns).
"""


class Positive:
    def __setattr__(self, name, value):
        # This runs for every assignment, e.g. p.age = 30 or p.age = -5,
        # before the value is actually stored anywhere.
        if name == "age" and value < 0:
            # Reject invalid data immediately, at the point of assignment,
            # rather than allowing a bad state to exist silently and
            # cause a confusing failure somewhere else later.
            raise ValueError("age >= 0 required")

        # Bypass custom write to prevent loops.
        # Writing self.name = value here would call THIS SAME
        # __setattr__ method again (since it is an assignment), which
        # would call itself again, forever. object.__setattr__ instead
        # performs Python's default, built-in write, storing the value
        # directly, without going through this override a second time.
        object.__setattr__(self, name, value)


if __name__ == "__main__":
    p = Positive()

    p.age = 30  # Success
    print("age set to:", p.age)

    try:
        p.age = -5  # ValueError!
    except ValueError as e:
        print("ValueError raised correctly:", e)

    # Attributes with any other name are unaffected by the age check,
    # and still go through the same bypass so they get stored normally.
    p.label = "adult"
    print("label set to:", p.label)
