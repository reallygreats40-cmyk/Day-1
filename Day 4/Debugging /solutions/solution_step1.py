"""
Step 1 of 8 - SOLUTION: Reproduce and Define the Symptom

The code is unchanged from the exercise - this step is about observing
and describing the symptom, not modifying code.

Model answers:
- Typical result: repeated runs cluster around 0.03-0.05 seconds on a
  typical laptop, with occasional higher outliers caused by background
  activity.
- Model problem statement: "process() takes about 40ms to process
  300,000 integers, which is too slow for a code path with a 10ms
  budget."
- Model environment note: quad-core laptop, otherwise idle, Python
  3.12, single run of 300,000 items - written down so later comparisons
  are apples-to-apples.
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
