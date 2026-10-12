"""Slide 3: synchronous version.

Three tasks run one after another; time.sleep() blocks the whole program.
Expected total time: about 3.0 seconds.
"""

import time

def fetch(name):
    print(f"start {name}")
    time.sleep(1)      # blocks the program
    print(f"done {name}")

def main():
    for name in ["A", "B", "C"]:
        fetch(name)

start = time.perf_counter()
main()
print(f"{time.perf_counter() - start:.1f} s")
# start A, done A, start B, done B,
# start C, done C, 3.0 s
