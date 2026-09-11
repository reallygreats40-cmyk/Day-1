"""
From: "Example Workload: app.py"

Deliberately contains repeated work, so a profiler has something
meaningful to reveal. Run this normally first with: python app.py
"""


def transform(value):
    return str(value).strip().upper()


def process(values):
    output = []
    for value in values:
        output.append(transform(value))
    return output


if __name__ == "__main__":
    values = range(100_000)
    result = process(values)
    print("items:", len(result))
