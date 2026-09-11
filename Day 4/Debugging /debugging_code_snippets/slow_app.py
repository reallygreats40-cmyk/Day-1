"""
From: "A Deliberately Slow Workload"

The code is correct; the investigation is about cost, not correctness.
Run with: python slow_app.py
"""
import time


def process(values):
    total = 0
    for value in values:
        # Repeated conversion inside a hot loop
        text = str(value)
        total += int(text)
    return total


if __name__ == "__main__":
    values = range(500_000)

    start = time.perf_counter()
    result = process(values)
    elapsed = time.perf_counter() - start

    print("result:", result)
    print("elapsed:", elapsed)

# try python -m pdb slow_app.py, then
'''
n (next line)
s (step into a function call)
c (continue running until the next breakpoint)c
p <expr> (print the value of an expression 
l (list the surrounding source code)
q (quit the debugger)

'''