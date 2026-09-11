import tracemalloc

tracemalloc.start()
before = tracemalloc.take_snapshot()

data = [str(i) * 10 for i in range(100_000)]

after = tracemalloc.take_snapshot()
stats = after.compare_to(before, "lineno")
for stat in stats[:10]:
    print(stat)

tracemalloc.stop()
