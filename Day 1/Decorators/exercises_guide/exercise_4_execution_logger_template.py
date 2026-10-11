# Exercise 4: Execution Logger with Metadata Preservation Template
# Target: Create a decorator that logs function metadata and parameters cleanly.

from functools import wraps

def execution_logger(func):
    """Logs the entry, exit, and parameters of the decorated function while preserving attributes."""
    # TODO: Use @wraps(func) to protect original docstring attributes
    pass

# Sample usage:
@execution_logger
def compute_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

if __name__ == "__main__":
    print(f"Docstring: {compute_area.__doc__}")
    compute_area(5, 10)
