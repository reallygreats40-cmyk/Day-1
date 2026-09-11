import time


def count_matches_list(values, targets):
    return sum(1 for value in values if value in targets)


def count_matches_set(values, targets):
    target_set = set(targets)
    return sum(1 for value in values if value in target_set)


def measure(fn, runs=7):
    times = []
    result = None

    for _ in range(runs):
        start = time.perf_counter()
        result = fn(values, targets)
        times.append(time.perf_counter() - start)

    return result, times


if __name__ == "__main__":
    values = list(range(200_000))
    targets = list(range(0, 200_000, 10))

    baseline_result, baseline_times = measure(count_matches_list)
    optimised_result, optimised_times = measure(count_matches_set)

    assert baseline_result == optimised_result

    baseline = min(baseline_times)
    optimised = min(optimised_times)
    speedup = baseline / optimised

    print("baseline min:", baseline)
    print("optimised min:", optimised)
    print("speedup:", speedup)
    print("correctness:", baseline_result == optimised_result)

    print("\nPerformance report")
    print("- Baseline:", baseline)
    print("- Hotspot: list membership testing")
    print("- Hypothesis: repeated O(n) membership checks dominate runtime")
    print("- Change: convert targets to a set")
    print("- Optimised:", optimised)
    print("- Speedup:", speedup)
    print("- Correctness verified:", baseline_result == optimised_result)
