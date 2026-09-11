"""
From: "Line-Level Profiling With line_profiler"

Install first with: python -m pip install line_profiler

The @profile decorator below is not a normal Python decorator you need
to import - kernprof injects it automatically when it runs this file,
so leave it exactly as-is.

Run with:
    kernprof -l -v calculate_script.py
"""


@profile
def calculate(values):
    result = []
    for value in values:
        text = str(value)
        cleaned = text.strip().lower()
        result.append(cleaned[::-1])
    return result


if __name__ == "__main__":
    calculate(range(50_000))
