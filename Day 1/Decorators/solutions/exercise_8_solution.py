# Exercise 8: Configurable Memoization Cache
# Task: Build an advanced memoization decorator that supports a shared, custom caching dictionary.

from functools import wraps


def memoize(custom_cache_store=None):
    """Advanced memoization decorator factory that supports an optional custom storage container."""
    def decorator(func):
        # Create a default enclosed dict if no custom cache is provided
        cache = custom_cache_store if custom_cache_store is not None else {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a serializable and hashable cache key from positional and keyword args
            # Sorting kwargs ensures identical keyword configurations yield matching keys
            key_args = args
            key_kwargs = tuple(sorted(kwargs.items()))
            cache_key = (key_args, key_kwargs)

            if cache_key in cache:
                print(f"[Memoize] Cache HIT for key: {cache_key}")
                return cache[cache_key]

            print(f"[Memoize] Cache MISS for key: {cache_key}. Computing...")
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result

        # Expose the active cache store object as a function attribute for debugging
        wrapper.cache_store = cache
        return wrapper
    return decorator


# Sample usage:
shared_database = {}


@memoize(custom_cache_store=shared_database)
def fibonacci(n):
    """Computes the nth Fibonacci number recursively with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(f"Result (Fib 10): {fibonacci(10)}")
    print(f"Total Cached Keys in Database: {len(shared_database)}")

# Explanation:
# This memoizer creates a hashable cache key from both positional and keyword arguments. By
# checking custom_cache_store, it allows injecting an external shared dictionary. This
# enables advanced architecture designs like crossing execution boundaries or sharing cache
# pools across different decorated targets. The wrapper.cache_store = cache assignment
# exposes the private dictionary as a callable attribute for real-time monitoring and
# inspection.
