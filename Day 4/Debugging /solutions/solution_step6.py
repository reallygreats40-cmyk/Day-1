"""
Step 6 of 8 - SOLUTION: Investigate Memory Growth

The code is unchanged - the task was to interpret the tracemalloc
output.

Model answers:
- Allocation site: the line inside the loop that builds each dict; the
  payload string (5x the length of the id) is the larger contributor.
- The objects remain alive because cache is a module-level list that
  is never cleared - every dict stays reachable for the life of the
  program.
- This is legitimate retention, not a leak: len(cache) matches the
  loop count exactly (50,000), with nothing meant to be discarded
  along the way.
- Bounded alternative: cap the list with a collections.deque(maxlen=..),
  or persist entries to disk incrementally instead of holding
  everything in memory at once.
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
