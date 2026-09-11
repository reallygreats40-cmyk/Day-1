"""
Step 3 of 8 - SOLUTION: Inspect Suspicious State with pdb

The code is unchanged. The comments below show the actual pdb session,
confirmed by running it with p index / p value / p total / c piped in.

Model answers:
- At the breakpoint: p index -> 3, p value -> -4, p total -> 14 (the
  sum of squares of 1, 2, and 3 so far).
- where shows process() was called directly from module level, at the
  print(process(values)) line.
- Conditional debugging is preferable because it lets the loop run at
  full speed until the one case actually worth investigating, instead
  of pausing on every iteration.
"""


def process(values):
    total = 0
    for index, value in enumerate(values):
        if value < 0:
            breakpoint()
        total += value * value
    return total


if __name__ == "__main__":
    values = [1, 2, 3, -4, 5]

    print(process(values))

    # (Pdb) p index    -> 3
    # (Pdb) p value    -> -4
    # (Pdb) p total    -> 14
    # (Pdb) c          -> 55
