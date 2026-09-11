"""
The Functional Mindset
======================

From: Functional Programming in Python -- notes deck
Topic: FUNCTIONAL MINDSET

Run this file directly: python 01_functional_mindset.py
"""

def add_tax(price, rate):
    return price * (1 + rate)

# Same inputs always produce the same output
print(round(add_tax(100, 0.16), 2))   # 116.0
print(round(add_tax(100, 0.16), 2))   # 116.0 again, guaranteed
