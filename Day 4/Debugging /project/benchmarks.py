import timeit

list_time = timeit.timeit(
    "value in values",
    setup="values = list(range(10000)); value = 9999",
    number=10000,
)
set_time = timeit.timeit(
    "value in values",
    setup="values = set(range(10000)); value = 9999",
    number=10000,
)

print("list:", list_time)
print("set :", set_time)
print("speedup:", list_time / set_time)
