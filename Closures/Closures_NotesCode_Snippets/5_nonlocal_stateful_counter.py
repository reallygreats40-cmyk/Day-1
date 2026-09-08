"""
Topic: The nonlocal statement modifies read-only parent variables

By default, a nested function can only READ an enclosing variable --
trying to assign to it directly would make Python treat it as a brand
new local variable instead (and raise UnboundLocalError if you tried to
use it before assigning). The `nonlocal` keyword tells Python to bind
to the existing enclosing-scope variable instead, allowing the inner
function to modify it. Note: `nonlocal` only reaches enclosing function
scopes, never the module-level global scope -- use `global` for that.

Run this file directly to see the output: python 5_nonlocal_stateful_counter.py
"""



def make_counter():
    count = 0

    def counter():
        nonlocal count  # bind to the enclosing scope's 'count', not a new local
        count += 1
        return count

    return counter


my_counter = make_counter()
print(my_counter())  # Outputs: 1
print(my_counter())  # Outputs: 2
print(my_counter())  # Outputs: 3
