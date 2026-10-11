"""
Exercise 7: Execution Timer (Prelude to Decorators)
Goal: Build a closure that prints the time taken to execute a target function.
"""
import time

def make_timer(func):
    """
    Returns a wrapped version of 'func' that prints its execution time.
    """
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"[{func.__name__}] Executed in {duration:.6f} seconds.")
        return result
    return timer_wrapper

# --- Verification ---
if __name__ == "__main__":
    def slow_sum(n):
        return sum(range(n))
        
    timed_sum = make_timer(slow_sum)
    print(timed_sum(1000000))  # Expected: Timing log followed by the sum
