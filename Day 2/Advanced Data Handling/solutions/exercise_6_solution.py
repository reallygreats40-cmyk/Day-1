import pandas as pd

def calculate_metrics_vectorized(df):
    # column-wise arithmetic runs on the whole column at once
    df["net_amount"] = df["amount"] * 0.90
    # transform("sum") aligns each group's total onto every row
    grp = df.groupby("category")["net_amount"]
    df["category_total"] = grp.transform("sum")
    # column divided by column: vectorized, no loop needed
    df["percentage_share"] = (
        df["net_amount"] / df["category_total"])
    return df

df_data = pd.DataFrame({
    "category": ["A", "A", "B", "B", "C"],
    "amount": [100.0, 200.0, 150.0, 50.0, 300.0],
})
print(calculate_metrics_vectorized(df_data))
