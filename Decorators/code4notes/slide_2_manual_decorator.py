"""
Slide 2: The Bridge - From Closures to Decorators
Goal: Understand the manual functional reassignment that underlies Python's decorator syntax.
"""

def null_decorator(func):
    """
    A basic decorator structure that wraps another function.
    """
    def wrapper():
        print("Before execution")
        func()  # Executes the closed-over target function
        print("After execution")
    return wrapper

def greet():
    print("Hello World")

if __name__ == "__main__":
    print("--- Running original greet() ---")
    greet()

    print("Running manually decorated greet() ---")
    # Manual decoration / reassignment
    decorated_greet = null_decorator(greet)
    decorated_greet()  # Prints log borders dynamically!
