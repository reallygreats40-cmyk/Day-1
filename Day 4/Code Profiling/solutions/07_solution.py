import time


def count_matches_list(values, targets):
    count = 0

    for value in values:
        if value in targets:
            count += 1

    return count


def count_matches_set(values, targets):
    target_set = set(targets)
    count = 0

    for value in values:
        if value in target_set:
            count += 1

    return count


if __name__ == "__main__":
    values = list(range(200_000))
    targets = list(range(0, 200_000, 10))

    start = time.perf_counter()
    baseline = count_matches_list(values, targets)
    baseline_time = time.perf_counter() - start

    start = time.perf_counter()
    optimised = count_matches_set(values, targets)
    optimised_time = time.perf_counter() - start

    assert baseline == optimised

    print("baseline:", baseline_time)
    print("optimised:", optimised_time)
    print("speedup:", baseline_time / optimised_time)
