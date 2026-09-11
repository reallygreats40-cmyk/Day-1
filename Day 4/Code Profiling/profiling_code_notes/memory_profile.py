"""
From: "cProfile + tracemalloc: The Right Tool for the Question"

CPU time and memory are different resources - a single profiler rarely
explains both. This file demonstrates the memory half; the CPU half is
run separately from the terminal (see the comment below).
"""
import tracemalloc

from app import process

# CPU question - run from the terminal instead:
#   python -m cProfile -s cumulative app.py

# Memory question:
import tracemalloc

tracemalloc.start()
before = tracemalloc.take_snapshot()

data = process(range(100_000))   # keep a reference — freed objects won't show up

after = tracemalloc.take_snapshot()
top_stats = after.compare_to(before, "lineno")

print(f'{"Size":>10}  {"Count":>8}  Location')
print("-" * 70)
for stat in top_stats[:10]:
    size_kb = stat.size_diff / 1024
    print(f'{size_kb:>8.1f} KB  {stat.count_diff:>8,}  {stat.traceback[0]}')

tracemalloc.stop()
