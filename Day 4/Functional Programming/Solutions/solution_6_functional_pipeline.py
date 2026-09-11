"""
Exercise 6: Composing a Functional Pipeline - Solution

Objective: Combine map, filter and reduce into a pipeline, then reproduce the same result using pandas.

Explanation: The pipeline filters out negative orders, applies the 5% charge with map, then reduce sums what is left. The pandas version reaches the same total with apply(): the lambda returns 0 for negative orders so they contribute nothing to the sum.
"""

from functools import reduce
import pandas as pd

orders = [12, -4, 30, 8, -2, 19]

pipeline_total = reduce(
    lambda acc, n: acc + n,
    map(lambda n: n * 1.05, filter(lambda n: n > 0, orders)),
    0
)

df = pd.DataFrame({"order": orders})
df["charged"] = df["order"].apply(lambda n: n * 1.05 if n > 0 else 0)
pandas_total = df["charged"].sum()


if __name__ == "__main__":
    print(round(pipeline_total, 2))   # 72.45
    print(round(pandas_total, 2))     # 72.45
