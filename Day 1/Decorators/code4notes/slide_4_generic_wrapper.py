"""
Slide 4: Generic Wrapping with *args and **kwargs
Goal: Implement parameter forwarding to support target functions with varying signatures.
"""

def audit_log(func):
    """
    A generic decorator that forwards parameters dynamically and preserves return values.
    """
    def wrapper(*args, **kwargs):
        print(f"Target '{func.__name__}' started.")
        result = func(*args, **kwargs)  # Forward parameters transparently
        print(f"Target '{func.__name__}' completed.")
        return result  # Preserve and return the target function's output
    return wrapper

@audit_log
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print("--- Running generic wrapped add_numbers ---")
    sum_result = add_numbers(10, 20)

    print(f"Result returned to caller: {sum_result}")

