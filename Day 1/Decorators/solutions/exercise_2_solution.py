# Exercise 2: Double Invocation Decorator
# Task: Create a decorator that executes the decorated target function twice on every call.

from functools import wraps


def double_invocation(func):
    """Executes the target function twice, returning the result of the second execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[DoubleInvocation] First execution start...")
        func(*args, **kwargs)  # First call (side-effects executed)
        print("[DoubleInvocation] Second execution start...")
        result = func(*args, **kwargs)  # Second call (capture output)
        return result
    return wrapper


# Sample usage:
@double_invocation
def send_alert(message):
    """Simulates sending an alert message."""
    print(f"ALERT: {message}")
    return "Alert Sent"


if __name__ == "__main__":
    status = send_alert("Database connection warning!")
    print(f"Final Status: {status}")

# Explanation:
# This solution modifies the target function's execution boundaries. Rather than altering
# parameters, the wrapper controls execution frequency. It triggers the original callable
# twice, capturing and returning the return value of only the second execution. This pattern
# is common in automatic reconnects and side-effect testing.
