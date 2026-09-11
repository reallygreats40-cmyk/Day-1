"""
Step 8 of 8 - Produce a Debugging and Optimisation Report

Create a concise report describing the complete investigation: the
original symptom, the evidence collected, the root cause, the change
made, correctness validation, and the performance improvement achieved.

Run with: python step8_report.py

Tasks:
- Fill in baseline_seconds, optimised_seconds, speedup, and
  correctness_verified using your own measured values from Step 7.
- State the test environment and workload size you used.
- State exactly what evidence supports your root-cause conclusion.
- State any limitations of your investigation, or possible follow-up
  work.
"""

report = {
    "symptom": "membership-heavy workload is slow",
    "baseline_seconds": None,
    "diagnostic_evidence": [
        "high repeated membership cost",
        "linear list membership",
        "large number of checks",
    ],
    "root_cause": "repeated O(n) membership searches",
    "change": "use a set for repeated membership tests",
    "optimised_seconds": None,
    "speedup": None,
    "correctness_verified": False,
}

if __name__ == "__main__":
    print(report)
