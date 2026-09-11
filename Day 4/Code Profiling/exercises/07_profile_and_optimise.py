import time


def count_matches(values, targets):
    count = 0

    for value in values:
        if value in targets:
            count += 1

    return count


if __name__ == "__main__":
    values = list(range(200_000))
    targets = list(range(0, 200_000, 10))

    # TASK:
    # 1. Benchmark the baseline.
    # 2. Profile it.
    # 3. Replace the lookup structure if semantics permit.
    # 4. Benchmark again.
    # 5. Assert that both versions return the same count.
    #
    # Explain why the new structure changes expected lookup
    # complexity and quantify the speedup.
