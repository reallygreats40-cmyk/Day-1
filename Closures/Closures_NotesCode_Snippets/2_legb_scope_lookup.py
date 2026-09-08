"""
Nested scopes resolve variables dynamically via LEGB lookup

LEGB = Local, Enclosing, Global, Built-in -- the order Python searches in
when looking up a variable name. Enclosing scope is the critical zone for
closures: an inner function can freely READ any variable in its enclosing
parent scopes, but cannot MODIFY it without the `nonlocal` keyword (see
5_nonlocal_stateful_counter.py for that).

Run this file directly to see the output: python 2_legb_scope_lookup.py
"""


def outer():
    # Enclosing scope variable
    message = 'Hi'

    def inner():
        # Local scope accessing the enclosing scope -- this is a read,
        # so no special keyword is needed
        print(message)

    inner()


outer()  # Outputs: 'Hi'
