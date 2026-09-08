"""
Topic: Python stores enclosed environment data inside the __closure__
attribute

Closures are not magic -- they are exposed transparently inside the
Python object architecture. The `__closure__` attribute is a tuple of
"cell" objects, each corresponding to one captured variable, and each
cell's `cell_contents` holds that variable's actual value. A function
that isn't a closure has `__closure__` set to None.

NOTE: the memory address shown for the cell object will differ every
time you run this (that's normal -- it's just where Python happened to
allocate that object in memory this run); the meaningful, stable part of
the output is the captured value itself, printed on the second line.

Run this file directly to see the output: python 4_closure_attribute_inspection.py
"""


def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier


double = make_multiplier(2)

# Inspect the internal closure cells
print(double.__closure__)
# Outputs something like: (<cell at 0x...: int object at 0x...>,)

# Inspect cell contents -- this is the actual captured value, '2'
cell = double.__closure__[0]
print(cell.cell_contents)  # Outputs: 2
