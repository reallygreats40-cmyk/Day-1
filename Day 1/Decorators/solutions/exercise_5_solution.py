# Exercise 5: Performance Monitor Stacking
# Task: Stack multiple decorators to measure call count and execution durations simultaneously.

import time
from functools import wraps


def count_calls(func):
    """Tracks the total number of times a function has been executed."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"[Count] '{func.__name__}' call count: {wrapper.calls}")
        return func(*args, **kwargs)
    wrapper.calls = 0  # Initialize stateful counter attribute
    return wrapper


def timer(func):
    """Measures and prints the execution duration of a function call."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"[Timer] '{func.__name__}' execution time: {duration:.6f} seconds")
        return result
    return wrapper


# Stack decorators: timer on top, count_calls on bottom
# Evaluation resolves as: timer(count_calls(heavy_computation))
@timer
@count_calls
def heavy_computation(n):
    """Simulates a heavy mathematical calculation loop."""
    total = 0
    for i in range(n):
        total += i * i
    return total


if __name__ == "__main__":
    heavy_computation(100000)
    heavy_computation(500000)

# Explanation:
# Stacking order maps to function nesting: timer(count_calls(heavy_computation)). When
# decorated this way, invoking heavy_computation() executes timer_wrapper, which measures
# how long it takes for count_calls_wrapper to execute (which in turn increments the counter
# and executes the target). If we reversed the stack, the counter wrapper would include the
# timer overhead inside its count boundary.
