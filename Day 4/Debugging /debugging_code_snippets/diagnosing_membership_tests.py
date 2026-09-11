"""
From: "Diagnosing Inefficient Membership Tests"

Instruments the workload first, before deciding to change its data
structure. Run with: python diagnosing_membership_tests.py
"""


def count_matches(values, targets):
    checks = 0
    matches = 0
    for value in values:
        checks += 1
        if value in targets:
            matches += 1
    return matches, checks


if __name__ == "__main__":
    values = range(100_000)
    targets = list(range(0, 100_000, 10))

    matches, checks = count_matches(values, targets)

    print("matches:", matches)
    print("membership checks:", checks)
