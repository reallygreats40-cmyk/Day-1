"""
Higher-Order Functions & partial
================================

From: Functional Programming in Python -- notes deck
Topic: HIGHER-ORDER FUNCTIONS

Run this file directly: python 07_partial_higher_order.py
"""

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))            # 25
print(cube(2))               # 8
