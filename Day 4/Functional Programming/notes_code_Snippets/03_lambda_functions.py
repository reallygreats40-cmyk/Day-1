"""
Lambda Functions
================

From: Functional Programming in Python -- notes deck
Topic: ANONYMOUS FUNCTIONS

Run this file directly: python 03_lambda_functions.py
"""

square = lambda x: x ** 2
print(square(5))            # 25

# Common use: as a sort key
people = [("Amy", 34), ("Bo", 22), ("Cy", 29)]
people_by_age = sorted(people, key=lambda person: person[1])
print(people_by_age)
# [('Bo', 22), ('Cy', 29), ('Amy', 34)]
