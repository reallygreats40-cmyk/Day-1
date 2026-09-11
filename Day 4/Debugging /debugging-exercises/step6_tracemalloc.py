"""
Step 6 of 8 - Investigate Memory Growth

Use tracemalloc to identify exactly where memory allocation increases
during repeated processing.

Run with: python step6_tracemalloc.py

Tasks:
- Identify the allocation site from the printed statistics.
- Explain why the cached objects remain alive for the rest of the
  program.
- Distinguish legitimate retained data from an actual memory leak.
- Propose a bounded or streaming alternative, if the complete history
  is not actually needed.
"""
import tracemalloc

cache = []


if __name__ == "__main__":
    tracemalloc.start()
    snapshot_before = tracemalloc.take_snapshot()

    for i in range(50_000):
        cache.append({"id": i, "payload": str(i) * 5})

    snapshot_after = tracemalloc.take_snapshot()

    for stat in snapshot_after.compare_to(
        snapshot_before, "lineno",
    )[:10]:
        print(stat)

    print("retained objects:", len(cache))

    tracemalloc.stop()
