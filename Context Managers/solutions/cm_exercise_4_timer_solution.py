# Exercise 4: Reusable Block Timer Profiler Solution
# Task: Create a class-based context manager named Timer that measures execution duration.

from time import perf_counter, sleep

class Timer:
    def __init__(self):
        self.start = 0.0
        self.elapsed = 0.0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.elapsed = perf_counter() - self.start
        print(f"[Timer] Process finished in {self.elapsed:.6f} seconds.")
        return False

# Verification
if __name__ == "__main__":
    with Timer() as timer:
        sleep(0.3)
    print(f"Time taken attribute verify: {timer.elapsed:.6f} seconds")
