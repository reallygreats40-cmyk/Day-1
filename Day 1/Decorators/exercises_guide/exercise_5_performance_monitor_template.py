# Exercise 5: Performance Monitor Stacking Template
# Target: Stack multiple decorators to measure call count and execution durations simultaneously.

import time
from functools import wraps

def count_calls(func):
    """Tracks the total number of times a function has been executed."""
    # TODO: Implement stateful call counter attribute
    pass

def timer(func):
    """Measures and prints the execution duration of a function call."""
    # TODO: Measure and log time.perf_counter() elapsed delta
    pass

# Stack decorators: timer on top, count_calls on bottom
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
