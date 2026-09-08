# Exercise 2: Double Invocation Decorator Template
# Target: Create a decorator that executes the decorated target function twice on every call.

from functools import wraps

def double_invocation(func):
    """Executes the target function twice, returning the result of the second execution."""
    # TODO: Execute func twice and return second output
    pass

# Sample usage:
@double_invocation
def send_alert(message):
    """Simulates sending an alert message."""
    print(f"ALERT: {message}")
    return "Alert Sent"

if __name__ == "__main__":
    status = send_alert("Database connection warning!")
    print(f"Final Status: {status}")
