"""
Exercise 6: Advanced pandas for Efficient Manipulation
Task: Optimize a loop-based pandas operation into vector ops.
"""
import pandas as pd

def calculate_metrics_loop(df):
    results = []
    for idx, row in df.iterrows():
        # Slow row-by-row logic
        net_amount = row["amount"] * 0.90
        results.append(net_amount)
    df["net_amount"] = results
    return df

# TODO: Refactor using column vectorization and transform
def calculate_metrics_vectorized(df):
    """
    - net_amount = amount * 0.90
    - category_total = total net_amount per category
    - percentage_share = each row's share of its category total
    """
    # Avoid iterrows! Use column expressions and groupby.transform
    pass

if __name__ == "__main__":
    df_data = pd.DataFrame({
        "category": ["A", "A", "B", "B", "C"],
        "amount": [100.0, 200.0, 150.0, 50.0, 300.0],
    })
    print(calculate_metrics_loop(df_data.copy()))
    vectorized_df = calculate_metrics_vectorized(df_data.copy())
    print(vectorized_df)
