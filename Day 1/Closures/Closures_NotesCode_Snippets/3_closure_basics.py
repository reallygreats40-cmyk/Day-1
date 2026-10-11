"""
 Inner functions capture enclosing state to form a closure

A closure is a nested function that retains access to variables in its
parent scope even after the parent function has finished executing.
Normally local variables are destroyed when a function exits -- closures
override this by packing the enclosing environment together with the
returned function, keeping it alive.

Run this file directly to see the output: python 3_closure_basics.py
"""


def make_multiplier(factor):
    # This variable is 'captured' by the inner function below
    def multiplier(number):
        return number * factor
    return multiplier


# Generate dynamic multiplier functions -- each one is a function factory
# result, with its own captured 'factor' value
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # Outputs: 20
print(triple(10))  # Outputs: 30
