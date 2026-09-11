"""
Lambda Functions in pandas
==========================

From: Functional Programming in Python -- notes deck
Topic: PANDAS INTEGRATION

Run this file directly: python 09_lambda_in_pandas.py
"""

import pandas as pd

df = pd.DataFrame({
    "name": ["Amy", "Bo", "Cy"],
    "price": [10, 20, 30],
})

df["price_with_tax"] = df["price"].apply(lambda p: p * 1.16)

df = df.assign(
    is_expensive=lambda d: d["price"] > 15
)
print(df)
#   name  price  price_with_tax  is_expensive
# 0  Amy     10            11.6         False
# 1   Bo     20            23.2          True
# 2   Cy     30            34.8          True
