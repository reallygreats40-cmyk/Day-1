import time

from app import process

start = time.perf_counter()
result = process(range(100_000))
elapsed = time.perf_counter() - start

print("result:", len(result))
print("elapsed:", elapsed, "seconds")
