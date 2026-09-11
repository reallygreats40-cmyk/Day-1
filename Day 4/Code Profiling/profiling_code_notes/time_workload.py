"""
From: "time.perf_counter(): Simple End-to-End Timing"

The simplest way to measure elapsed time around a larger operation.
Run with: python perf_counter_timing.py
"""
import time

from app import process

start = time.perf_counter()

result = process(range(100_000))

elapsed = time.perf_counter() - start

print("result:", len(result))
print("elapsed:", elapsed, "seconds")
