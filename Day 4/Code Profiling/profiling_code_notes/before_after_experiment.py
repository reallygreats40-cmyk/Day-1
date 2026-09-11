"""
From: "A Complete Before/After Experiment"

Never report an optimisation without measuring both versions under the
same conditions. Reuses the functions and data from
membership_testing_optimisation.py, the same way the deck's own
"separate the workload from the driver" principle recommends.

Run with: python before_after_experiment.py
"""
import time

from membership_testing_optimisation import (
    count_matches,
    count_matches_fast,
    values,
    targets,
    target_set,
)


def measure(fn, runs=7):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        result = fn()
        times.append(time.perf_counter() - start)
    return result, min(times)


if __name__ == "__main__":
    baseline_result, baseline = measure(
        lambda: count_matches(values, targets)
    )
    fast_result, optimised = measure(
        lambda: count_matches_fast(values, target_set)
    )

    assert baseline_result == fast_result

    print("baseline :", baseline)
    print("optimised:", optimised)
    print("speedup  :", baseline / optimised)
