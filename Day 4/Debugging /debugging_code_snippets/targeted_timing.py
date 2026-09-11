"""
From: "Targeted Timing with perf_counter()"

Measures only the operation relevant to the hypothesis being tested.
Run with: python targeted_timing.py
"""
import time


def normalise(value):
    start = time.perf_counter()
    result = str(value).strip().lower()
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    total_time = 0.0
    for value in range(50_000):
        _, elapsed = normalise(value)
        total_time += elapsed

    print("measured normalise time:", total_time)
