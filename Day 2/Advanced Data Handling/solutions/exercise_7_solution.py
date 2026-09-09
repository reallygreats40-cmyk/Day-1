import pandas as pd

def create_unoptimized_df():
    data = {
        "status_code": [200, 404, 500, 200] * 1000,
        "region_label": ["north_america", "europe", "asia",
                          "south_america"] * 1000,
        "temperature": [25.5, 12.0, 30.2, 18.1] * 1000,
    }
    return pd.DataFrame(data)

def optimize_dataframe_dtypes(df):
    # store each unique string once, reuse a small code
    df["region_label"] = df["region_label"].astype("category")
    # whole numbers that comfortably fit in a smaller range
    df["status_code"] = df["status_code"].astype("int16")
    # decimals that don't need float64's extra precision
    df["temperature"] = df["temperature"].astype("float32")
    return df

df_raw = create_unoptimized_df()
mem_before = df_raw.memory_usage(deep=True).sum()
# deep=True gives honest sizing for object/string columns
df_opt = optimize_dataframe_dtypes(df_raw.copy())
mem_after = df_opt.memory_usage(deep=True).sum()
savings = (mem_before - mem_after) / mem_before * 100
print(f"Before: {mem_before/1024:.2f} KB")
print(f"After:  {mem_after/1024:.2f} KB")
print(f"Savings: {savings:.2f}%")
