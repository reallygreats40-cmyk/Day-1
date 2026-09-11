"""
From: "Diagnosing Accidental Retention"

A cache or global collection can keep objects alive for the entire life
of the process. Run with: python diagnosing_accidental_retention.py
"""

cache = {}


def add_result(key, value):
    cache[key] = value


if __name__ == "__main__":
    for i in range(100_000):
        add_result(i, {"value": i})

    print("cache size:", len(cache))

    # Diagnostic question:
    # Does the application really need every entry?
