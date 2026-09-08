# Exercise 1: Basic Uppercase Decorator Template
# Target: Write a basic decorator that converts the string output of a function to uppercase.

from functools import wraps

def uppercase_decorator(func):
    """Converts the returned string value of the target function to uppercase."""
    # TODO: Implement the decorator wrapper closure
    pass

# Sample usage:
@uppercase_decorator
def get_welcome_message(name):
    """Returns a personalized welcome message string."""
    return f"Welcome, {name}! Let's learn decorators."

if __name__ == "__main__":
    result = get_welcome_message("delegate")
    print(f"Result: {result}")
    print(f"Preserved Docstring: {get_welcome_message.__doc__}")
