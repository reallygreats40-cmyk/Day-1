"""
Step 4 of 8 - SOLUTION: Add Targeted Timing and Call-Count Diagnostics

The code is unchanged - the task was to interpret the numbers it
produces.

Model answers:
- Typical result: calls: 50000, measured transform time: roughly
  0.01-0.02 seconds total - under 1 microsecond per call on average.
- Since each call is already this cheap, call frequency (not per-call
  cost) is what would dominate if this function were invoked far more
  often.
- perf_counter() itself has a small overhead; when timing something
  this fast, that overhead is a meaningful fraction of what gets
  measured.
- If the operation became much faster still, aggregate timing across a
  batch (as done here) rather than timing every single call, to keep
  the overhead ratio low.
"""
import time

calls = 0


def expensive_transform(value):
    global calls
    calls += 1
    start = time.perf_counter()
    result = str(value).strip().lower()[::-1]
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    values = range(50_000)
    total_time = 0.0

    for value in values:
        _, elapsed = expensive_transform(value)
        total_time += elapsed

    print("calls:", calls)
    print("measured transform time:", total_time)
