"""Slide 8, version 2: a running total kept inside a class.

Works, and each object keeps its own total, but a class, __init__, self
and a method call are needed for just one behaviour.
"""

class Tally:
    def __init__(self):
        self.total = 0

    def add(self, amount):
        self.total += amount
        return self.total

shop = Tally()
print(shop.add(10))  # Outputs: 10
print(shop.add(5))   # Outputs: 15
