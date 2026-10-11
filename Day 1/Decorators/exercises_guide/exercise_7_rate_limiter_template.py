# Exercise 7: Token Bucket Rate Limiter Template
# Target: Build a stateful, rate-limiting decorator factory using closure states.

import time
from functools import wraps

def limit_rate(max_calls=5, period_seconds=2):
    """Decorator factory that limits calls to a function within a specific time window."""
    # TODO: Manage enclosing timestamps sliding window array
    pass

# Sample usage:
@limit_rate(max_calls=3, period_seconds=2)
def read_secure_vault():
    """Simulates retrieving highly sensitive credentials."""
    return "Vault Data"

if __name__ == "__main__":
    # Test rate limits
    for i in range(5):
        try:
            print(f"Attempt {i+1}: {read_secure_vault()}")
            time.sleep(0.2)
        except RuntimeError as e:
            print(f"Attempt {i+1} Blocked: {e}")
