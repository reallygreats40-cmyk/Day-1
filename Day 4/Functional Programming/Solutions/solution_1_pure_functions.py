"""
Exercise 1: Pure Functions & Avoiding Side Effects - Solution

Objective: Practice writing a pure function, and refactor an impure function so it no longer mutates its input.

Explanation: calculate_total() only reads its arguments and returns a new value, so it is pure. apply_discount() is fixed with a list comprehension, which builds a brand new list instead of writing into the caller's list, so the original list is left untouched.
"""

def calculate_total(prices, tax_rate):
    return sum(prices) * (1 + tax_rate)


def apply_discount(prices, discount):
    return [p * (1 - discount) for p in prices]


if __name__ == "__main__":
    print(calculate_total([10, 20], 0.1))   # 33.0

    original = [100, 200]
    discounted = apply_discount(original, 0.1)
    print(discounted)   # [90.0, 180.0]
    print(original)     # [100, 200] (unchanged)
