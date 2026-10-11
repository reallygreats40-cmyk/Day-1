"""
Topic: Function decorators leverage closure mechanics to wrap behaviors

A decorator is simply a function that takes another function as input,
wraps it in new behaviour, and returns the wrapper -- and that wrapper is
itself a closure, keeping a live reference to the original 'func' it was
given. This is the exact same closure mechanism shown in
3_closure_basics.py, applied to build the @decorator pattern. *args and
**kwargs let the wrapper accept whatever arguments the wrapped function
needs, without having to know its signature in advance.

Run this file directly to see the output: python 6_decorator_via_closure.py
"""


def logged(func):
    # Wrapper closure captures 'func' from the enclosing scope
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Finished {func.__name__}')
        return result
    return wrapper


@logged
def add(a, b):
    return a + b


print(add(5, 7))
# Outputs:
# Calling add
# Finished add
# 12
