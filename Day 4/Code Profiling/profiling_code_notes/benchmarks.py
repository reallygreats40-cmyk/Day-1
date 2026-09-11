"""
From: "timeit: Micro-Benchmark a Small Operation"

Compares list membership testing against set membership testing under
identical conditions. Run with: python timeit_benchmark.py
"""
import timeit

# Time membership check ('in') on a list of 10,000 ints, run 10,000 times
list_time = timeit.timeit(
    "value in values",
    setup="values = list(range(10000)); value = 9999",  # worst case: last element
    number=10000,
)

# Time the same membership check, but on a set instead of a list
set_time = timeit.timeit(
    "value in values",
    setup="values = set(range(10000)); value = 9999",
    number=10000,
)

print("list:", list_time)      # total seconds for 10,000 list lookups
print("set :", set_time)       # total seconds for 10,000 set lookups
print("speedup:", list_time / set_time)  # how many times faster the set is