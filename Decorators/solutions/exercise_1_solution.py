# Exercise 1: Basic Uppercase Decorator
# Task: Write a basic decorator that converts the string output of a function to uppercase.

from functools import wraps


def uppercase_decorator(func):
    """Converts the returned string value of the target function to uppercase."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Invoke the original function
        original_output = func(*args, **kwargs)

        # Validate that the output is indeed a string before calling .upper()
        if isinstance(original_output, str):
            return original_output.upper()
        return original_output
    return wrapper


# Sample usage:
@uppercase_decorator
def get_welcome_message(name):
    """Returns a personalized welcome message string."""
    return f"Welcome, {name}! Let's learn decorators."


if __name__ == "__main__":
    result = get_welcome_message("delegate")
    print(f"Result: {result}")
    print(f"Preserved Docstring: {get_welcome_message.__doc__}")

# Explanation:
# This solution demonstrates a basic outer-inner functional closure. The uppercase_decorator
# takes func as an argument. Inside, the wrapper capture closure executes the target,
# intercepts the returned value, checks its datatype, and returns the uppercase conversion.
# The @wraps decorator prevents original function namespace data loss.
