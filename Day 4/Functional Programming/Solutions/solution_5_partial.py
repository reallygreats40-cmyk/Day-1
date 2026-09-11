"""
Exercise 5: Higher-Order Functions & functools.partial - Solution

Objective: Build a higher-order function and use functools.partial to pre-configure it.

Explanation: convert_currency() is a general-purpose function that needs both an amount and a rate. partial() locks in the rate for each currency, producing to_usd and to_gbp: ordinary-looking functions that only still need an amount.
"""

from functools import partial

def convert_currency(amount, rate):
    return amount * rate


to_usd = partial(convert_currency, rate=1.09)
to_gbp = partial(convert_currency, rate=0.79)


if __name__ == "__main__":
    print(round(to_usd(100), 2))   # 109.0
    print(round(to_gbp(100), 2))   # 79.0
