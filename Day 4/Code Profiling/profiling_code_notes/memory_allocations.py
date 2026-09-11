"""
From: "tracemalloc: Identify the Biggest Allocation Sources"

Shows file, line number, size difference, and allocation count for the
largest changes between two snapshots.
Run with: python tracemalloc_biggest_sources.py
"""
import tracemalloc

tracemalloc.start()  # begin recording memory allocations

# Snapshot of memory usage before the allocation we want to measure
snapshot1 = tracemalloc.take_snapshot()

# The allocation under test: 50,000 dicts, each holding an int and a string
items = [{"id": i, "text": str(i)} for i in range(50_000)]

# Snapshot of memory usage after the allocation
snapshot2 = tracemalloc.take_snapshot()

# Compare the two snapshots line-by-line, sorted by size difference (biggest first)
for stat in snapshot2.compare_to(snapshot1, "lineno")[:5]:  # top 5 changes only
    print(
        "file:", stat.traceback,     # where the allocation happened (file:line)
        "size_diff:", stat.size_diff,   # extra bytes allocated on this line
        "count_diff:", stat.count_diff,  # extra number of objects allocated on this line
    )

tracemalloc.stop()  # stop recording (frees tracemalloc's own overhead)