"""
Step 7 of 8 - SOLUTION: Fix the Root Cause and Validate

The code below is already the fix - Step 7 asks you to implement and
measure it, which this file does directly.

Model answers:
- Root cause: count_matches_list is O(n x m) - for each of 200,000
  values, up to 20,000 targets are scanned.
- count_matches_set makes each check O(1) on average via hashing, so
  total cost drops to roughly O(n).
- Semantics preserved: set(targets) contains exactly the same elements
  as the list, so membership results are identical - assert a == b
  proves this for this run.
- Example measured result on this run: baseline ~24.7s, optimised
  ~0.006s, speedup ~4150x. Exact numbers vary by machine.
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

    print("baseline:", baseline)      # e.g. 24.7
    print("optimised:", optimised)    # e.g. 0.006
    print("speedup:", baseline / optimised)   # e.g. 4150.0
