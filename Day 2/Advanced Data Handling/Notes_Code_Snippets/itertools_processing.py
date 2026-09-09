"""
Advanced Data Handling & Manipulation
Topic: Itertools -- itertools for Memory Friendly Processing

"""

from itertools import islice, groupby, accumulate


def main():
    # 1. Bounded consumption with islice
    stream = (x * x for x in range(100)) # generator object

    first_five = list(islice(stream, 5))  # only 5 values ever computed, list(islice(stream, 2, 10))
    print(f"First five squares: {first_five}")

    # 2. Grouping sequential records with groupby
    data = [
        {"category": "A", "val": 10},
        {"category": "A", "val": 20},
        {"category": "B", "val": 15},
        {"category": "B", "val": 30},
    ]
    # groupby expects sorted inputs by the key function
    data.sort(key=lambda x: x["category"])
    for key, group in groupby(data, key=lambda x: x["category"]):
        group_items = list(group)
        print(f"Category {key} has items: {group_items}")

    # 3. Running calculations with accumulate
    values = [10, 20, 30, 40]
    running_totals = list(accumulate(values))  # cumulative sum by default
    print(f"Running totals: {running_totals}")


if __name__ == "__main__":
    main()
