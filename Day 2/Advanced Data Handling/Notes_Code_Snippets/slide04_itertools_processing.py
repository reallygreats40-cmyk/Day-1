from itertools import islice, groupby, accumulate

def main():
    # 1. islice: take only what you need from a stream
    stream = (x * x for x in range(100))
    first_five = list(islice(stream, 5))   # only 5 values computed
    print(f"First five squares: {first_five}")

    # 2. groupby: groups neighbouring items with the same key
    data = [
        {"category": "B", "val": 15},
        {"category": "A", "val": 10},
        {"category": "B", "val": 30},
        {"category": "A", "val": 20},
    ]
    data.sort(key=lambda row: row["category"])   # sort first!
    for key, group in groupby(data, key=lambda row: row["category"]):
        vals = [row["val"] for row in group]
        print(f"Category {key}: {vals}")

    # 3. accumulate: running totals over a stream
    daily_sales = [100, 250, 75, 300]
    print(f"Running total: {list(accumulate(daily_sales))}")

if __name__ == "__main__":
    main()
