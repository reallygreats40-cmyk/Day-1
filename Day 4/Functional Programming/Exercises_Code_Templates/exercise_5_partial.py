"""
Exercise 5: Higher-Order Functions & functools.partial

Objective: Build a higher-order function and use functools.partial to pre-configure it.
Instructions: Complete convert_currency(), then use partial() to build to_usd() and to_gbp().
"""

from functools import partial

def convert_currency(amount, rate):
    # TODO: return amount converted using rate (amount * rate)
    pass

# TODO: use partial() to create to_usd(amount), fixing rate=1.09
to_usd = None

# TODO: use partial() to create to_gbp(amount), fixing rate=0.79
to_gbp = None


if __name__ == "__main__":
    print(round(to_usd(100), 2))   # Expected: 109.0
    print(round(to_gbp(100), 2))   # Expected: 79.0
