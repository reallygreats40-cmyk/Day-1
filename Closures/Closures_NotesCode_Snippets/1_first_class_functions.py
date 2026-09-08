"""
Functions behave as first-class objects in the Python runtime

Key principle: in Python, parentheses () execute a function. Passing the
name without parentheses passes the actual function object reference.

Run this file directly to see the output: python 1_first_class_functions.py
"""


def shout(text):
    return text.upper()


# Assign to a variable -- no parentheses, so this passes the function
# object itself, not the result of calling it
yell = shout
print(yell('hello'))  # Outputs: 'HELLO'



def greet(func):
    # Pass function as an argument
    print(func('hi there'))


greet(shout)  # Outputs: 'HI THERE'
