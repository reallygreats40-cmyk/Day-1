"""
Exercise 1: Pure Functions & Avoiding Side Effects

Objective: Practice writing a pure function, and refactor an impure function so it no longer mutates its input.
Instructions: Complete calculate_total(prices, tax_rate) so it returns the total cost including tax. Then fix apply_discount() so it returns a NEW list instead of mutating the list it was given.
"""

def calculate_total(prices, tax_rate):
    # TODO: return the sum of prices, increased by tax_rate
    # e.g. calculate_total([10, 20], 0.1) -> 33.0
    pass


# TODO: fix apply_discount so it no longer mutates the input list.
# It should return a NEW list of discounted prices instead.
def apply_discount(prices, discount):
    for i in range(len(prices)):
        # side effect: this line mutates prices!
        prices[i] = prices[i] * (1 - discount)
    return prices


if __name__ == "__main__":
    print(calculate_total([10, 20], 0.1))   # Expected: 33.0

    original = [100, 200]
    discounted = apply_discount(original, 0.1)
    print(discounted)   # Expected: [90.0, 180.0]
    print(original)
    # Expected: [100, 200] (unchanged!)
