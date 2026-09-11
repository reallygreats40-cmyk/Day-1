"""
Composing map, filter, reduce
=============================

From: Functional Programming in Python -- notes deck
Topic: COMPOSITION

Run this file directly: python 08_composing_pipelines.py
"""

from functools import reduce

orders = [15, -3, 42, 8, -1, 23]

pipeline = reduce(
    lambda acc, n: acc + n,
    map(lambda n: n * 1.16,
        filter(lambda n: n > 0, orders)),
    0
)
print(round(pipeline, 2))    # 102.08

# The same result, written as a comprehension
total = sum(n * 1.16 for n in orders if n > 0)
print(round(total, 2))       # 102.08
