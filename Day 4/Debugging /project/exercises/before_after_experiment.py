import time

from membership_optimisation import count_matches, count_matches_fast


def measure(fn, runs=7):
    times = []
    result = None
    for _ in range(runs):
        start = time.perf_counter()
        result = fn()
        times.append(time.perf_counter() - start)
    return result, min(times)


if __name__ == "__main__":
    values = range(200_000)
    targets = list(range(0, 200_000, 10))
    target_set = set(targets)

    baseline_result, baseline = measure(lambda: count_matches(values, targets))
    fast_result, optimised = measure(lambda: count_matches_fast(values, target_set))

    assert baseline_result == fast_result
    print("baseline :", baseline)
    print("optimised:", optimised)
    print("speedup  :", baseline / optimised)
