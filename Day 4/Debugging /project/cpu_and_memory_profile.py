# CPU question:
#   python -m cProfile -s cumulative app.py

# Memory question:
import tracemalloc

from app import process

tracemalloc.start()
before = tracemalloc.take_snapshot()

# run workload here
process(range(50_000))

after = tracemalloc.take_snapshot()
print(after.compare_to(before, "lineno")[:10])
tracemalloc.stop()
