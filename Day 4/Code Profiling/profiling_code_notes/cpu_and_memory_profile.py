# CPU question:
# python -m cProfile -s cumulative app.py

# Memory question:
import tracemalloc

tracemalloc.start()
before = tracemalloc.take_snapshot()

# run workload here
data = [str(i) for i in range(100_000)]

after = tracemalloc.take_snapshot()
print(after.compare_to(before, "lineno")[:5])
tracemalloc.stop()