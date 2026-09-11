"""
Step 5 of 8 - SOLUTION: Diagnose Repeated Work in a Hot Path

The code is unchanged - the task was to reason about the cost, not to
fix it yet (the fix comes in Step 7).

Model answers:
- Cost estimate: 100,000 values, each scanning up to 10,000 target
  items - on the order of hundreds of millions of comparisons in the
  worst case.
- Hypothesis: converting targets to a set would make each membership
  check O(1) on average instead of O(n), removing that scaling problem
  entirely.
- This hypothesis is confirmed by measurement in Step 7, not assumed -
  the implementation is deliberately left unchanged here.
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
