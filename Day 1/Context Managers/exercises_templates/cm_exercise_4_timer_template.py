# Exercise 4: Reusable Block Timer Profiler Template
# Task: Create a class-based context manager named Timer that measures execution duration.

from time import perf_counter

class Timer:
    def __init__(self):
        self.elapsed = 0.0

    def __enter__(self):
        # TODO: Record start time
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        # TODO: Record elapsed duration
        pass

# Verification Code
if __name__ == "__main__":
    import time
    with Timer() as timer:
        time.sleep(0.3)
    print(f"Time taken: {timer.elapsed:.6f} seconds")
