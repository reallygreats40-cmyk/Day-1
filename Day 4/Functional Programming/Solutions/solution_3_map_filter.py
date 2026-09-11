"""
Exercise 3: Transforming and Filtering with map() and filter() - Solution

Objective: Use map() and filter() to transform and select data without writing a manual for-loop.

Explanation: map() applies the Celsius-to-Fahrenheit formula to every value in one pass. filter() keeps only the values where the predicate (c > 20) is True. Both return lazy iterators, so list() is used to see the results.
"""

temperatures_c = [0, 21, 33, -5, 40, 15]

temperatures_f = map(lambda c: c * 9/5 + 32, temperatures_c)
warm_days = filter(lambda c: c > 20, temperatures_c)


if __name__ == "__main__":
    print(list(temperatures_f))
    # [32.0, 69.8, 91.4, 23.0, 104.0, 59.0]

    print(list(warm_days))
    # [21, 33, 40]
