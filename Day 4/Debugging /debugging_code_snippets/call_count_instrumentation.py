"""
From: "Call-Count Instrumentation"

Determines whether a suspicious function is simply being called too often.
Run with: python call_count_instrumentation.py
"""

calls = 0


def normalise(value):
    global calls
    calls += 1
    return str(value).strip().lower()


def process(values):
    return [normalise(value) for value in values]


if __name__ == "__main__":
    values = range(100_000)
    result = process(values)

    print("items:", len(result))
    print("normalise calls:", calls)
