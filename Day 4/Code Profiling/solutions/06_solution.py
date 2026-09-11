import tracemalloc


if __name__ == "__main__":
    tracemalloc.start()

    snapshot_before = tracemalloc.take_snapshot()

    data = [str(i) * 10 for i in range(100_000)]

    snapshot_after = tracemalloc.take_snapshot()

    for stat in snapshot_after.compare_to(
        snapshot_before,
        "lineno",
    )[:10]:
        print(stat)

    del data
    tracemalloc.stop()
