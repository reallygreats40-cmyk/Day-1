"""
From: "Example Optimisation: Repeated Membership Testing"

Compares list membership (O(n)) against set membership (O(1) average).
This module can be run directly, or imported by
before_after_experiment.py to reuse its functions and data.
"""

values = range(200_000)
targets = list(range(0, 200_000, 10))
target_set = set(targets)


def count_matches(values, targets):
    count = 0
    for value in values:
        if value in targets:
            count += 1
    return count


def count_matches_fast(values, target_set):
    return sum(1 for v in values if v in target_set)


if __name__ == "__main__":
    # Baseline:
    print(count_matches(values, targets))

    # Candidate optimisation:
    print(count_matches_fast(values, target_set))
