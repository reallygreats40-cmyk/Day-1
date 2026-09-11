def calculate(values):
    result = []

    for value in values:
        cleaned = str(value).strip().lower()
        result.append(cleaned[::-1])

    return result


if __name__ == "__main__":
    values = list(range(100_000))
    result = calculate(values)

    print("items:", len(result))

    # If line_profiler is installed, profile calculate()
    # using the current supported runner/decorator workflow.
    #
    # The goal is to identify which line accounts for the
    # meaningful share of calculate() execution time.
