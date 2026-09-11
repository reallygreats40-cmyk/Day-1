"""
Exercise 3: Transforming and Filtering with map() and filter()

Objective: Use map() and filter() to transform and select data without writing a manual for-loop.
Instructions: Complete temperatures_f using map(), and warm_days using filter().
"""

temperatures_c = [0, 21, 33, -5, 40, 15]

# TODO: use map() to convert every Celsius value to Fahrenheit
# formula: F = C * 9/5 + 32
temperatures_f = None

# TODO: use filter() to keep only temperatures above 20 Celsius
warm_days = None


if __name__ == "__main__":
    print(list(temperatures_f))
    # Expected: [32.0, 69.8, 91.4, 23.0, 104.0, 59.0]

    print(list(warm_days))
    # Expected: [21, 33, 40]
