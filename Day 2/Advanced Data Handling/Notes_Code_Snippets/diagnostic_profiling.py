"""
Advanced Data Handling & Manipulation
Topic: Diagnostic Profiling -- Memory Tracking and Diagnostic Audits

"""

import tracemalloc


def execute_heavy_allocation():
    # Materializes a large list in memory
    return [x * 2 for x in range(500_000)]


def main():
    # Start tracking memory allocations
    tracemalloc.start()

    # Initial snapshot
    initial_snapshot = tracemalloc.take_snapshot()

    # Perform allocation
    data = execute_heavy_allocation()

    # Get current and peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current Memory Usage: {current / (1024 * 1024):.2f} MB")
    print(f"Peak Memory Allocation: {peak / (1024 * 1024):.2f} MB")

    # Take final snapshot and stop
    final_snapshot = tracemalloc.take_snapshot()
    top_stats = final_snapshot.compare_to(initial_snapshot, "lineno")
    print("\nTop memory-growth locations since the initial snapshot:")
    for stat in top_stats[:3]:
        print(stat)
    tracemalloc.stop()


if __name__ == "__main__":
    main()
