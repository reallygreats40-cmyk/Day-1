"""
Step 1 of 8 - Reproduce and Define the Symptom

Create a slow function and establish a repeatable baseline. Describe the
symptom in measurable terms, rather than saying only that the program
is slow.

Run with: python step1_reproduce.py

Tasks:
- Run the workload several times and record a typical elapsed time.
- Write a one-sentence performance problem statement, based on a
  measurable symptom rather than a feeling.
- Note the machine and conditions you tested under, so this baseline
  can be reproduced later.
"""
import time


def process(values):
    total = 0
    for value in values:
        total += (value * value) % 97
    return total


if __name__ == "__main__":
    values = list(range(300_000))

    start = time.perf_counter()
    result = process(values)
    elapsed = time.perf_counter() - start

    print("result:", result)
    print("elapsed:", elapsed)
