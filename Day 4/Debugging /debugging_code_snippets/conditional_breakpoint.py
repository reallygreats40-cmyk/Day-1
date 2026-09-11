"""
From: "Conditional Debugging in a Large Loop"

Stops only when index == 10_000 and value > 90_000, instead of on
every one of the 100,000 iterations.

Run with: python conditional_breakpoint.py
"""


def process(values):
    total = 0
    for index, value in enumerate(values):
        if index == 10_000 and value > 90_000:
            breakpoint()
        total += value
    return total


if __name__ == "__main__":
    values = list(range(100_000))
    # With a plain range, index and value are always equal, so the
    # condition below could never actually become true. This single
    # override guarantees the breakpoint has a real case to catch,
    # while leaving the rest of the sequence untouched.
    values[10_000] = 91_000

    print(process(values))
