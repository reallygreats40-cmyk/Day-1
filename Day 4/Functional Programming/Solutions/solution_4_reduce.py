"""
Exercise 4: Aggregating Data with reduce() - Solution

Objective: Use functools.reduce to fold a sequence of items down to a single aggregated value.

Explanation: The first reduce() accumulates a running total, starting from 0. The second reduce() has no initial value, so it starts from the first basket item and keeps whichever of the two items being compared has the higher price.
"""

from functools import reduce

basket = [
    {"item": "bread", "price": 2.5},
    {"item": "milk", "price": 1.8},
    {"item": "eggs", "price": 3.2},
]

total_price = reduce(lambda acc, item: acc + item["price"], basket, 0)
most_expensive = reduce(
    lambda a, b: a if a["price"] > b["price"] else b, basket
)


if __name__ == "__main__":
    print(round(total_price, 2))     # 7.5
    print(most_expensive["item"])    # eggs
