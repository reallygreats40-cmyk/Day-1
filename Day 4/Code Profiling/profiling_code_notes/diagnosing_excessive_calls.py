"""
From: "Example: Diagnosing Excessive Calls"

A high call count is often a stronger clue than a slightly slow
individual call. Profile this with:
    python -m cProfile -s tottime diagnosing_excessive_calls.py
"""


def normalise(value):
    return str(value).strip().lower()


def process(values):
    result = []
    for value in values:
        result.append(normalise(value))
    return result


if __name__ == "__main__":
    values = range(200_000)
    result = process(values)

    print(len(result))
