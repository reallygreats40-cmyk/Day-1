"""Slide 8, version 1: a running total kept with a plain function and global state.

Works, but the total lives in a global variable: any code can change it,
and the program can only hold one running total.
"""

total = 0

def add(amount):
    global total
    total += amount
    return total

print(add(10))  # Outputs: 10
print(add(5))   # Outputs: 15
