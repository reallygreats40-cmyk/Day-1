# Exercise 6: Stateful Retry Decorator Factory Template
# Target: Write a configurable decorator factory that retries failing operations.

import time
from functools import wraps

def retry(max_attempts=3, delay_seconds=1):
    """A decorator factory that retries execution on exception failures up to max_attempts."""
    # TODO: Implement three-tier factory structure
    pass

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
