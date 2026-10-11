# Exercise 7: Sliding Window Rate Limiter
# Task: Build a stateful, rate-limiting decorator factory using closure states.

import time
from functools import wraps


def limit_rate(max_calls=5, period_seconds=2):
    """Decorator factory that limits calls to a function within a specific time window."""
    def decorator(func):
        # Stateful closure boundary: timestamps list persists inside outer scope
        call_timestamps = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()

            # Filter out timestamps outside our active sliding window
            # Use non-local list mutations to filter expired timestamps
            expired_threshold = now - period_seconds
            call_timestamps[:] = [t for t in call_timestamps if t > expired_threshold]

            if len(call_timestamps) >= max_calls:
                raise RuntimeError(
                    f"Rate Limit Exceeded: Function '{func.__name__}' is restricted to "
                    f"{max_calls} invocations every {period_seconds} seconds."
                )

            # Record current invocation timestamp and execute
            call_timestamps.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Sample usage:
@limit_rate(max_calls=3, period_seconds=2)
def read_secure_vault():
    """Simulates querying a secure storage system."""
    return "Decrypted Auth Token: s3cr3t_v@ult"


if __name__ == "__main__":
    for i in range(5):
        try:
            print(f"Call {i+1}: {read_secure_vault()}")
            time.sleep(0.3)
        except RuntimeError as e:
            print(f"Blocked call {i+1}: {e}")

# Explanation:
# By capturing a mutable list (call_timestamps) inside the decorator's enclosing scope, we
# hide stateful memory safe from external manipulation. The call_timestamps[:] slice
# assignment alters the original list in-place. If the window has more timestamps than
# max_calls, the wrapper blocks execution and raises an error, safeguarding APIs or
# resource-intensive calculations.
