"""
reduce(): Aggregating a Sequence
================================

From: Functional Programming in Python -- notes deck
Topic: HIGHER-ORDER FUNCTIONS

Run this file directly: python 06_reduce_aggregate.py
"""

from functools import reduce

prices = [10, 20, 30]
total = reduce(lambda acc, p: acc + p, prices, 0)
print(total)                 # 60

# Same idea, finding the maximum
values = [4, 9, 2, 7]
largest = reduce(lambda acc, v: v if v > acc else acc, values)
print(largest)                # 9
