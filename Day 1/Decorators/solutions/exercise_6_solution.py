# Exercise 6: Stateful Retry Decorator Factory
# Task: Write a configurable decorator factory that retries failing operations.

import time
from functools import wraps


def retry(max_attempts=3, delay_seconds=1):
    """A decorator factory that retries execution on exception failures up to max_attempts."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"[Retry] Attempt {attempts}/{max_attempts} failed with error: {e}")
                    if attempts >= max_attempts:
                        raise e
                    print(f"[Retry] Sleeping for {delay_seconds}s before next attempt...")
                    time.sleep(delay_seconds)
        return wrapper
    return decorator


# Sample usage:
@retry(max_attempts=3, delay_seconds=0.5)
def unstable_network_call(url):
    """Simulates an unstable HTTP endpoint call."""
    import random
    if random.random() > 0.3:
        raise ConnectionError("Timeout attempting to resolve endpoint.")
    return f"Response received from {url}!"


if __name__ == "__main__":
    try:
        msg = unstable_network_call("https://api.python-decorators.academy")
        print(f"Success Message: {msg}")
    except ConnectionError as e:
        print(f"Operation aborted after all retries: {e}")

# Explanation:
# This three-tier architecture is a standard pattern for configurable decorator factories.
# The top tier, retry(), accepts configurations like max_attempts, returning the standard
# decorator closure. Python then invokes this inner decorator, passing the target function
# object, which finally returns the wrapper enclosing both configurations and callables.
