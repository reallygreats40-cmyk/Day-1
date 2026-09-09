"""
Advanced Data Handling & Manipulation
Topic: Pandas Diagnostics -- Narrow dtypes and Categorical Optimization

"""

import pandas as pd


def main():
    # Write a dummy sales CSV
    df_dummy = pd.DataFrame({
        "category": ["electronics", "books", "electronics", "clothing"] * 100,
        "amount": [299.99, 15.50, 45.00, 120.00] * 100
    })
    df_dummy.to_csv("large_sales.csv", index=False)

    #print(df_dummy.info())

    # Explicit narrow datatypes definition
    dtype_spec = {
        "category": "category",  # cuts down repetitive string storage
        "amount": "float32"      # 32-bit floats instead of default float64
    }

    totals = {}
    # Load and process CSV in chunks -- never all 400 rows at once
    for chunk in pd.read_csv("large_sales.csv", dtype=dtype_spec, chunksize=100):
        # Category aggregation inside each chunk
        partial = chunk.groupby("category", observed=True)["amount"].sum()
        for category, amount in partial.items():
            totals[category] = totals.get(category, 0.0) + amount

    print(f"Combined totals across all chunks: {totals}")


if __name__ == "__main__":
    main()
