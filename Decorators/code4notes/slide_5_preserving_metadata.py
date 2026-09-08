"""
Slide 5: Preserving Metadata - @functools.wraps
Goal: Prevent function metadata loss (like names and docstrings) after decoration.
"""
from functools import wraps

def audited(func):
    """
    A generic decorator that logs execution while preserving metadata.
    """
    @wraps(func)  # Restores original namespace attributes onto the wrapper
    def wrapper(*args, **kwargs):
        """Audits execution"""
        return func(*args, **kwargs)
    return wrapper

@audited
def calculate_total():
    """Computes shopping basket items"""
    pass

if __name__ == "__main__":
    print("--- Inspecting function metadata ---")
    print(f"Function Name: {calculate_total.__name__}")  # Expected: calculate_total (not 'wrapper')
    print(f"Function Docstring: {calculate_total.__doc__}")  # Expected: Computes shopping basket items
