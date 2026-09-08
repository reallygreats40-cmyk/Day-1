# Exercise 3: Type Validation Decorator Template
# Target: Write a decorator that validates the datatype of a function's arguments.

from functools import wraps

def type_check_string(func):
    """Validates that the first positional argument passed to the function is a string."""
    # TODO: Verify first positional argument args[0] is of type str
    pass

# Sample usage:
@type_check_string
def process_username(username):
    """Processes and registers a unique username."""
    print(f"Username '{username}' has been successfully processed.")
    return True

if __name__ == "__main__":
    try:
        process_username("alex_python")  # Success
        process_username(12345)          # Raises TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")
