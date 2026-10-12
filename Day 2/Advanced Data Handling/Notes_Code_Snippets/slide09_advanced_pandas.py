import pandas as pd

def main():
    df = pd.DataFrame({
        "category": ["A", "A", "B", "B", "C"],
        "amount": [10.0, 20.0, 15.0, 35.0, 50.0],
    })

    # 1. Vectorised column arithmetic (no Python loop)
    df["amount_with_vat"] = df["amount"] * 1.2

    # 2. Named aggregation: one summary row per category
    summary = df.groupby("category", as_index=False).agg(
        total=("amount", "sum"),
        average=("amount", "mean"),
    )
    print(summary)

    # 3. transform: per-group result, aligned to every original row
    df["group_total"] = df.groupby("category")["amount"].transform("sum")
    df["share"] = df["amount"] / df["group_total"]
    print(df)

if __name__ == "__main__":
    main()
