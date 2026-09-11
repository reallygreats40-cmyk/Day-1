"""
Step 8 of 8 - SOLUTION: Produce a Debugging and Optimisation Report

The report below is completed with example values measured in
Step 7 - this is what a finished report looks like.

Model answers:
- speedup = baseline_seconds / optimised_seconds, calculated directly
  from the Step 7 measurements.
- Test environment: state the machine, OS, and Python version, plus
  the exact workload size (200,000 values, 20,000 targets) - anyone
  should be able to repeat this run.
- Evidence for the root cause: Step 5's checks counter confirmed one
  membership check per value; Step 7's timing directly measured the
  O(n) vs O(1) difference that Step 5 predicted.
- Limitations: a single-machine, single-run measurement; a follow-up
  could test with a very small target set, where the set-conversion
  overhead itself might start to dominate.
"""

report = {
    "symptom": "membership-heavy workload is slow",
    "baseline_seconds": 24.7,
    "diagnostic_evidence": [
        "high repeated membership cost",
        "linear list membership",
        "large number of checks",
    ],
    "root_cause": "repeated O(n) membership searches",
    "change": "use a set for repeated membership tests",
    "optimised_seconds": 0.006,
    "speedup": 4150.0,
    "correctness_verified": True,
}

if __name__ == "__main__":
    print(report)
