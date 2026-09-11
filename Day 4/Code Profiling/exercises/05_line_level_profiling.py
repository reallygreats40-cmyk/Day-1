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

    # TASK:
    # If line_profiler is installed, profile calculate().
    #
    # Install if required:
    # python -m pip install line_profiler
    #
    # Use the current line_profiler workflow supported by
    # your installed version.
    #
    # Identify the line with the most meaningful contribution
    # to total execution time.
