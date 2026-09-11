try:
    profile  # noqa: F821 - injected automatically by kernprof
except NameError:
    def profile(func):
        """No-op fallback so this file also runs with plain `python`,
        not only with `kernprof`."""
        return func


@profile
def calculate(values):
    result = []
    for value in values:
        text = str(value)
        cleaned = text.strip().lower()
        result.append(cleaned[::-1])
    return result


if __name__ == "__main__":
    output = calculate(range(50_000))
    print("processed:", len(output))

# Run and view the line-by-line report with line_profiler installed:
#   kernprof -l -v calculate_script.py
