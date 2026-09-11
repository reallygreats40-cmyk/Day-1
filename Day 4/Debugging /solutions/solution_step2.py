"""
Step 2 of 8 - SOLUTION: Build a Controlled Diagnostic Benchmark

The benchmark code is unchanged from the exercise - the task was to
reason about the method, not to change the code.

Model answers:
- Why a changed workload invalidates comparison: a timing difference
  could then come from the different input, not from any real
  improvement - the two numbers would no longer be comparable.
- Noise sources: other running applications, CPU frequency/thermal
  throttling, virtual machine or container scheduling, and disk or
  swap activity.
- min(times) approximates the best-case cost with system noise
  stripped out; avg(times) is more useful once consistency, not just
  best case, also matters.
"""
import time

from solution_step1 import process


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
