"""
Exercise 7: Memory Management and dtype Specifications
Task: Optimize a memory-heavy DataFrame with compact dtypes.
"""
import pandas as pd

def create_unoptimized_df():
    data = {
        "status_code": [200, 404, 500, 200] * 1000,
        "region_label": ["north_america", "europe", "asia",
                         "south_america"] * 1000,
        "temperature": [25.5, 12.0, 30.2, 18.1] * 1000,
    }
    return pd.DataFrame(data)

# TODO: Implement a memory-optimized converter
def optimize_dataframe_dtypes(df):
    """
    - region_label -> 'category'
    - status_code -> 'int16'
    - temperature -> 'float32'
    """
    pass

if __name__ == "__main__":
    df_raw = create_unoptimized_df()
    mem_before = df_raw.memory_usage(deep=True).sum()
    print(f"Before: {mem_before / 1024:.2f} KB")
    df_opt = optimize_dataframe_dtypes(df_raw.copy())
    if df_opt is not None:
        mem_after = df_opt.memory_usage(deep=True).sum()
        print(f"After: {mem_after / 1024:.2f} KB")
        savings = (mem_before - mem_after) / mem_before * 100
        print(f"Savings: {savings:.2f}%")
