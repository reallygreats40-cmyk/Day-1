"""
Step 4 of 8 - Add Targeted Timing and Call-Count Diagnostics

Instrument a suspicious function to determine whether the problem is
excessive execution frequency, expensive individual calls, or both.

Run with: python step4_timing.py

Tasks:
- Decide whether call frequency or per-call cost is the more important
  diagnostic clue here.
- Explain why instrumentation itself can distort very small timings.
- Consider how you would reduce the overhead of this instrumentation if
  the operation being measured became much faster.
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
