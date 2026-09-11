import tracemalloc


if __name__ == "__main__":
    tracemalloc.start()

    snapshot_before = tracemalloc.take_snapshot()

    # Run the workload being investigated.
    data = [str(i) * 10 for i in range(100_000)]

    snapshot_after = tracemalloc.take_snapshot()

    for stat in snapshot_after.compare_to(
        snapshot_before,
        "lineno",
    )[:10]:
        print(stat)

    # TASK:
    # Identify the largest allocation sites.
    # Decide whether the allocations are necessary.
    # Remember that tracemalloc focuses on Python allocations.
    # It does not account for every native allocation.

    del data
    tracemalloc.stop()
