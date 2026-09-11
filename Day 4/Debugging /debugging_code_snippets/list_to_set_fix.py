"""
From: "From List to Set Membership"

Measures both implementations directly, and confirms the fix preserves
correctness. Run with: python list_to_set_fix.py
"""
import time


def slow(values, targets):
    return sum(value in targets for value in values)


def fast(values, targets):
    target_set = set(targets)
    return sum(value in target_set for value in values)


if __name__ == "__main__":
    values = range(200_000)
    targets = list(range(0, 200_000, 10))

    start = time.perf_counter()
    a = slow(values, targets)
    slow_time = time.perf_counter() - start

    start = time.perf_counter()
    b = fast(values, targets)
    fast_time = time.perf_counter() - start

    assert a == b

    print("slow:", slow_time)
    print("fast:", fast_time)
    print("speedup:", slow_time / fast_time)
