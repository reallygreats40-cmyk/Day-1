"""
Exercise 7: Execution Timer (Prelude to Decorators)
Objective: Build a closure make_timer(func) that intercepts execution to measure and log the timing of a target function in seconds.
"""
import time

def make_timer(func):
    def timer_wrapper(*args, **kwargs):
        # TODO: Record start time, execute func, record end time,
        # print the duration, and return the function result.
        pass
    return timer_wrapper

# --- Verification ---
if __name__ == "__main__":
    @make_timer  # Equivalent to: timed_sum = make_timer(sum_func)
    def slow_sum(n): 
        return sum(range(n))
        
    slow_sum(1000000)
