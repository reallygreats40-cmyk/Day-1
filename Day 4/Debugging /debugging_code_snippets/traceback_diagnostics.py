"""
From: "Traceback Diagnostics"

Uses traceback information to identify exactly where repeated failures
originate. Run with: python traceback_diagnostics.py
"""
import traceback


def divide(values):
    result = []
    for value in values:
        try:
            result.append(100 / value)
        except ZeroDivisionError:
            traceback.print_exc()
            result.append(None)
    return result


if __name__ == "__main__":
    print(divide([10, 5, 0, 20]))
