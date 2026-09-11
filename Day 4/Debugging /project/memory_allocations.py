import tracemalloc

tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()

items = [{"id": i, "text": str(i)} for i in range(50_000)]

snapshot2 = tracemalloc.take_snapshot()
for stat in snapshot2.compare_to(snapshot1, "lineno")[:5]:
    print(
        "file:", stat.traceback,
        "size_diff:", stat.size_diff,
        "count_diff:", stat.count_diff,
    )
