"""
From: "Exceptions as a Performance Clue"

Measures whether an exception-heavy path is occurring more than expected.
Run with: python exceptions_performance_clue.py
"""

attempts = 0
failures = 0


def parse_value(text):
    global attempts, failures
    attempts += 1
    try:
        return int(text)
    except ValueError:
        failures += 1
        return 0


if __name__ == "__main__":
    values = ["10", "20", "bad", "30", "bad"]
    result = [parse_value(value) for value in values]

    print("attempts:", attempts)
    print("failures:", failures)
    print("failure rate:", failures / attempts)
