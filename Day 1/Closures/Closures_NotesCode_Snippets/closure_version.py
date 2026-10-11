"""Slide 8, version 3: a running total kept inside a closure.

Private state in a few lines: each call to make_tally() returns a new,
independent total that is called like an ordinary function.
"""

def make_tally():
    total = 0
    def add(amount):
        nonlocal total
        total += amount
        return total
    return add

shop = make_tally()
cafe = make_tally()
print(shop(10))  # Outputs: 10
print(shop(5))   # Outputs: 15
print(cafe(3))   # Outputs: 3
