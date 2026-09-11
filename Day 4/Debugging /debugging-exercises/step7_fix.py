"""
Step 7 of 8 - Fix the Root Cause and Validate

Implement a targeted optimisation for the membership-test problem from
Step 5. Preserve the result, and measure before and after.

Run with: python step7_fix.py
This takes around 25 seconds to run - that slowness is the whole point,
since it is exactly what the fix in this exercise addresses.

Tasks:
- Explain the root cause in algorithmic terms (its Big-O cost), not
  just "it was slow."
- Explain why the optimisation preserves the required membership
  semantics.
- Compare the measured baseline and optimised times, and repeat the
  experiment if the difference looks small.
"""
import time


def count_matches_list(values, targets):
    return sum(1 for value in values if value in targets)


def count_matches_set(values, targets):
    target_set = set(targets)
    return sum(1 for value in values if value in target_set)


if __name__ == "__main__":
    values = list(range(200_000))
    targets = list(range(0, 200_000, 10))

    start = time.perf_counter()
    a = count_matches_list(values, targets)
    baseline = time.perf_counter() - start

    start = time.perf_counter()
    b = count_matches_set(values, targets)
    optimised = time.perf_counter() - start

    assert a == b

    print("baseline:", baseline)
    print("optimised:", optimised)
    print("speedup:", baseline / optimised)
