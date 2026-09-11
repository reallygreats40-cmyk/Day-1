def count_matches(values, targets):
    count = 0
    for value in values:
        if value in targets:
            count += 1
    return count


def count_matches_fast(values, target_set):
    return sum(1 for v in values if v in target_set)


if __name__ == "__main__":
    values = range(200_000)
    targets = list(range(0, 200_000, 10))

    # Baseline:
    print(count_matches(values, targets))

    # Candidate optimisation:
    target_set = set(targets)
    print(count_matches_fast(values, target_set))
