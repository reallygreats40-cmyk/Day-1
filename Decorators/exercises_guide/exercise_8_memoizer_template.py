# Exercise 8: Configurable Memoization Cache Template
# Target: Build an advanced memoization decorator that supports a shared, custom caching dictionary.

from functools import wraps

def memoize(custom_cache_store=None):
    """Advanced memoization decorator factory that supports an optional custom storage container."""
    # TODO: Construct a cache dictionary and support shared injection
    pass

shared_database = {}

@memoize(custom_cache_store=shared_database)
def fibonacci(n):
    """Calculates the nth Fibonacci number recursively with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    # Warm up cache
    print(f"Fibonacci(30): {fibonacci(30)}")
    print(f"Shared Database Cache Size: {len(shared_database)}")
