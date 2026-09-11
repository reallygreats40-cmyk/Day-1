"""
Step 2 of 8 - Build a Controlled Diagnostic Benchmark

Create a benchmark that separates running the workload from reporting
on it, and repeats the same operation several times. This becomes your
controlled diagnostic environment.

This snippet assumes process() from Step 1 is available in the same
file - here, it is imported directly from step1_reproduce.py.

Run with: python step2_benchmark.py

Tasks:
- Keep the workload completely unchanged while diagnosing the problem -
  only the measurement code should differ.
- Explain why changing the workload between runs would make a
  before/after comparison meaningless.
- Identify sources of measurement noise, such as other running
  applications, CPU frequency scaling, or background processes.
"""
import time

from step1_reproduce import process


def benchmark(fn, runs=10):
    times = []
    result = None
    for _ in range(runs):
        start = time.perf_counter()
        result = fn()
        times.append(time.perf_counter() - start)
    return result, times


if __name__ == "__main__":
    values = list(range(300_000))
    result, times = benchmark(lambda: process(values))

    print("min:", min(times))
    print("avg:", sum(times) / len(times))
    print("result:", result)
