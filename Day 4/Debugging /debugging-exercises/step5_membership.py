"""
Step 5 of 8 - Diagnose Repeated Work in a Hot Path

Investigate a function that repeatedly performs a membership test. Use
reasoning, targeted counters, and measurement to determine whether the
data structure is contributing to the slowdown.

Run with: python step5_membership.py

Tasks:
- Estimate the cost of list membership testing at this scale.
- Form a hypothesis about an alternative data structure - but do not
  change the implementation yet.
- Explain why repeated list membership testing can become expensive as
  the list grows.
"""


def count_matches(values, targets):
    checks = 0
    count = 0
    for value in values:
        checks += 1
        if value in targets:
            count += 1
    return count, checks


if __name__ == "__main__":
    values = list(range(100_000))
    targets = list(range(0, 100_000, 10))

    result, checks = count_matches(values, targets)

    print("matches:", result)
    print("membership checks:", checks)
