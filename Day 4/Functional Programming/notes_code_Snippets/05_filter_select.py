"""
filter(): Selecting Elements
============================

From: Functional Programming in Python -- notes deck
Topic: HIGHER-ORDER FUNCTIONS

Run this file directly: python 05_filter_select.py
"""

numbers = [1, -4, 7, 0, -2, 9]

positives = filter(lambda n: n > 0, numbers)
print(list(positives))      # [1, 7, 9]

# filter(None, ...) drops falsy values
mixed = [0, 1, "", "hi", None, 5]
print(list(filter(None, mixed)))
# [1, 'hi', 5]
