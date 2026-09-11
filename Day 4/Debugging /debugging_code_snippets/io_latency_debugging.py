"""
From: "Debugging I/O-Like Latency"

CPU debugging alone may not explain user-visible waiting time.
Run with: python io_latency_debugging.py
"""
import time


def external_operation():
    # Simulate an external wait
    time.sleep(0.05)
    return "ok"


if __name__ == "__main__":
    start = time.perf_counter()
    result = external_operation()
    elapsed = time.perf_counter() - start

    print("result:", result)
    print("external wait:", elapsed)
