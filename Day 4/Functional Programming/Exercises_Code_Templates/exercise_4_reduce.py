"""
Exercise 4: Aggregating Data with reduce()

Objective: Use functools.reduce to fold a sequence of items down to a single aggregated value.
Instructions: Complete total_price and most_expensive using reduce().
"""

from functools import reduce

basket = [
    {"item": "bread", "price": 2.5},
    {"item": "milk", "price": 1.8},
    {"item": "eggs", "price": 3.2},
]

# TODO: use reduce() to compute the total price of everything in the basket
total_price = None

# TODO: use reduce() to find the most expensive item (the dict itself)
most_expensive = None


if __name__ == "__main__":
    print(round(total_price, 2))     # Expected: 7.5
    print(most_expensive["item"])    # Expected: eggs
