"""
From: "Memory Debugging with tracemalloc"

Compares memory snapshots taken before and after the workload runs.
Run with: python tracemalloc_memory_debugging.py
"""
import tracemalloc

if __name__ == "__main__":
    tracemalloc.start()
    before = tracemalloc.take_snapshot()

    data = [
        {"id": i, "payload": str(i) * 10}
        for i in range(50_000)
    ]

    after = tracemalloc.take_snapshot()

    for stat in after.compare_to(before, "lineno")[:10]:
        print(stat)

    print("objects retained:", len(data))

    tracemalloc.stop()
