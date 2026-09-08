# Exercise 4: Execution Logger with Metadata Preservation
# Task: Create a decorator that logs function metadata and parameters cleanly.

from functools import wraps


def execution_logger(func):
    """Logs the entry, exit, and parameters of the decorated function while preserving attributes."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--- [LOG] Entering function: {func.__name__} ---")
        print(f"[LOG] Arguments: positional={args}, keyword={kwargs}")

        # Execute the function and capture output
        try:
            result = func(*args, **kwargs)
            print(f"[LOG] Exiting function: {func.__name__} -> Return Value: {result}")
            return result
        except Exception as e:
            print(f"[LOG] Function {func.__name__} raised exception: {e}")
            raise e
    return wrapper


# Sample usage:
@execution_logger
def compute_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width


if __name__ == "__main__":
    print(f"Docstring: {compute_area.__doc__}")
    compute_area(5, 10)

# Explanation:
# This logging pattern demonstrates full envelope wrapping. By capturing variables and
# formatting logs on entry and exit, the wrapper creates clean execution metrics. Using
# try-except ensures exceptions are logged while preserving standard traceback bubbling via
# raise e. Importantly, @wraps(func) copies metadata like __doc__ and __name__.
