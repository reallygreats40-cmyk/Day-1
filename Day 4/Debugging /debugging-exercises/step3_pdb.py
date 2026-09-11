"""
Step 3 of 8 - Inspect Suspicious State with pdb

Use breakpoint() to stop inside a function the moment a suspicious
condition occurs. The aim is to understand why the program is taking
an unexpected path.

Run with: python step3_pdb.py
Execution pauses automatically at the negative value in the list.

Tasks:
- At the breakpoint, inspect index, value, and total using p.
- Use where to see the full call stack, and c to continue execution
  once you understand what happened.
- Explain why conditional debugging (stopping only when a specific
  condition is met) is preferable to stopping on every iteration.
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
