"""
Dynamic Extension: binding methods dynamically at runtime
=============================================================

WHAT THIS SHOWS
----------------
Functions in Python are ordinary, first-class objects: they can be
stored in variables, passed around, and, importantly here, assigned as
an attribute on a class after that class already exists. The moment a
plain function is assigned to a class attribute whose first parameter is
`self`, Python treats it exactly like any method defined directly inside
the class body: every existing and future instance of that class can
call it, and `self` is filled in automatically.

Report starts out completely empty (`pass`). The function `summary` is
written on its own, with no connection to Report at all, until the line
`Report.summary = summary` attaches it. From that point on, every
Report instance, including ones created earlier, has a working
`.summary()` method.

WHY THIS MATTERS
----------------
This lets behavior be added to a class after the fact, from code that
may not even be in the same file as the original class definition. That
is the mechanism underneath several common patterns: plugin systems that
attach handler methods to a shared base class, monkey-patching in tests,
and frameworks that generate methods programmatically instead of asking
a developer to hand-write each one.

WHERE THIS SHOWS UP IN REAL CODE
---------------------------------
- Plugin or mixin systems, where loading a plugin module attaches new
  capabilities to an existing base class instead of requiring every
  plugin to subclass something.
- API client libraries that generate one method per API endpoint from a
  specification file (OpenAPI, GraphQL schema) at import time, rather
  than someone hand-writing hundreds of near-identical methods.
- Monkey-patching in tests: temporarily replacing or adding a method on
  a class to control its behavior for a single test, then restoring it.
- Retrofitting new functionality onto a class you cannot or would rather
  not edit directly, such as one from a third-party library.

A CAUTION FROM THE NOTES
--------------------------
Because this technique adds methods that are invisible in the class's
own source file, the notes stress keeping a clear naming convention and
a real testing strategy, so it stays easy to trace where a given method
actually came from.
"""


class Report:
    pass


def summary(self):
    # A completely ordinary function. Nothing about its definition ties
    # it to Report; the connection is made only by the assignment below.
    return "report ready"


# Bind function as a class method.
# This single line is doing the same job the `class` body would do for
# a method written directly inside it: it stores `summary` under the
# name "summary" in Report's own namespace.
Report.summary = summary


if __name__ == "__main__":
    r = Report()
    print(r.summary())  # 'report ready'

    # The binding applies to the CLASS, so it is visible on every
    # instance, including ones that already existed before the
    # assignment happened.
    r2 = Report()
    print(r2.summary())  # 'report ready'
