import pandas as pd

def main():
    # Create a sample CSV with 400 rows
    pd.DataFrame({
        "category": ["electronics", "books", "electronics", "clothing"] * 100,
        "amount": [299.99, 15.50, 45.00, 120.00] * 100,
    }).to_csv("large_sales.csv", index=False)

    # Narrow types, applied while the file is read
    dtype_spec = {"category": "category", "amount": "float32"}

    # Read 100 rows at a time and combine the partial totals
    totals = {}
    for chunk in pd.read_csv("large_sales.csv", dtype=dtype_spec,
                             chunksize=100):
        partial = chunk.groupby("category", observed=True)["amount"].sum()
        for category, amount in partial.items():
            totals[category] = totals.get(category, 0) + float(amount)
    print({k: round(v, 2) for k, v in totals.items()})

    # Compare memory: default types vs narrow types
    wide = pd.read_csv("large_sales.csv")
    narrow = pd.read_csv("large_sales.csv", dtype=dtype_spec)
    print(wide.memory_usage(deep=True).sum(), "bytes (default types)")
    print(narrow.memory_usage(deep=True).sum(), "bytes (narrow types)")

if __name__ == "__main__":
    main()
