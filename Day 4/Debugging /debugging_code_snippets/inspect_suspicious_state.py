"""
From: "Hands-On: Inspect Suspicious State"

Run this normally. Execution pauses automatically the moment a negative
value is encountered. At the breakpoint, try: p index, p value, p total,
then where, then n to step, then c to continue.

Run with: python inspect_suspicious_state.py
"""


def calculate(values):
    total = 0
    for index, value in enumerate(values):
        if value < 0:
            breakpoint()
        total += value * value
    return total


if __name__ == "__main__":
    values = [2, 4, 7, -3, 8]

    print("result:", calculate(values))
