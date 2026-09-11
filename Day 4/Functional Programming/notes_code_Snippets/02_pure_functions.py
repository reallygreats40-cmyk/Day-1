"""
Pure Functions & Side Effects
=============================

From: Functional Programming in Python -- notes deck
Topic: CORE CONCEPT

Run this file directly: python 02_pure_functions.py
"""

total_calls = 0

def impure_add(a, b):
    global total_calls
    total_calls += 1        # side effect: mutates external state
    return a + b

def pure_add(a, b):
    return a + b            # no side effect, same result always

print(pure_add(2, 3))       # 5
print(pure_add(2, 3))       # 5, no hidden state involved
