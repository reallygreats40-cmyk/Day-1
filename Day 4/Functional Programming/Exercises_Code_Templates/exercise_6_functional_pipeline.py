"""
Exercise 6: Composing a Functional Pipeline

Objective: Combine map, filter and reduce into a pipeline, then reproduce the same result using pandas.
Instructions: Complete pipeline_total using filter/map/reduce, then complete pandas_total using a DataFrame and apply().
"""

from functools import reduce
import pandas as pd

orders = [12, -4, 30, 8, -2, 19]

# TODO: build a pipeline using filter, map and reduce that:
#   1. keeps only positive orders
#   2. applies a 5% service charge to each (multiply by 1.05)
#   3. sums the result into a single total
pipeline_total = None

# TODO: repeat the same calculation using a pandas DataFrame:
#   - df already has a column "order" from orders
#   - add a column "charged" using .apply() with a lambda that applies
#     the 5% service charge, but only to positive orders (use 0 otherwise)
#   - sum the "charged" column into pandas_total
df = pd.DataFrame({"order": orders})
pandas_total = None


if __name__ == "__main__":
    print(round(pipeline_total, 2))   # Expected: 72.45
    print(round(pandas_total, 2))     # Expected: 72.45
