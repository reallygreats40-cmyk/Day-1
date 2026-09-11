"""
map(): Transforming a Sequence
==============================

From: Functional Programming in Python -- notes deck
Topic: HIGHER-ORDER FUNCTIONS

Run this file directly: python 04_map_transform.py
"""

prices = [10, 20, 30]

with_tax = map(lambda p: p * 1.16, prices)
print(list(with_tax))       # [11.6, 23.2, 34.8]

# map with two iterables
quantities = [2, 1, 5]
totals = list(map(lambda p, q: p * q, prices, quantities))
print(totals)                # [20, 20, 150]
