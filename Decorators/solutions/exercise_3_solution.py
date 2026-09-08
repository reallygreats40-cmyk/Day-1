# Exercise 3: Type Validation Decorator
# Task: Write a decorator that validates the datatype of a function's arguments.

from functools import wraps


def type_check_string(func):
    """Validates that the first positional argument passed to the function is a string."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise ValueError("No positional arguments provided to type-check.")

        first_arg = args[0]
        if not isinstance(first_arg, str):
            raise TypeError(
                f"Type Validation Error: First argument must be of type 'str', "
                f"but received '{type(first_arg).__name__}'.")

        return func(*args, **kwargs)
    return wrapper


# Sample usage:
@type_check_string
def process_username(username):
    """Processes and registers a unique username."""
    print(f"Username '{username}' has been successfully processed.")
    return True


if __name__ == "__main__":
    try:
        process_username("alex_python")  # Success
        process_username(12345)  # Raises TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")

# Explanation:
# This guard pattern uses decorators to validate data pre-conditions before executing inner
# business logic. The wrapper intercepts the positional arguments tuple args. By checking
# args[0], it forces type validation, raising a TypeError early to prevent runtime issues
# deeper in the execution pipeline.
