"""
Advanced Data Handling & Manipulation
Topic: Advanced Pandas -- Vectorization and Groupby Transformations

"""

import pandas as pd


def main():
    df = pd.DataFrame({
        "category": ["A", "A", "B", "B", "C"],
        "amount": [10.0, 20.0, 15.0, 35.0, 50.0],
    })

    # 1. Groupby named aggregation -- collapses to one row per category
    summary = (
        df.groupby("category", as_index=False)
        .agg(
            total=("amount", "sum"),
            average=("amount", "mean")
        )
    )
    print("Grouped Summary:")
    print(summary)

    # 2. Groupby transform (retains index alignment for original dataframe)
    df["group_total"] = df.groupby("category")["amount"].transform("sum")
    df["share"] = df["amount"] / df["group_total"]
    print("\nOriginal rows with group_total and share:")
    print(df)


if __name__ == "__main__":
    main()
