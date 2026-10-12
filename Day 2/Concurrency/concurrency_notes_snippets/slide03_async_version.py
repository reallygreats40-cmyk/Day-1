"""Slide 3: asynchronous version.

The same three tasks on one thread; await asyncio.sleep() yields control,
so the waits overlap. Expected total time: about 1.0 second.
"""

import asyncio, time

async def fetch(name):
    print(f"start {name}")
    await asyncio.sleep(1)  # yields control
    print(f"done {name}")

async def main():
    await asyncio.gather(
        fetch("A"), fetch("B"), fetch("C"))

start = time.perf_counter()
asyncio.run(main())
print(f"{time.perf_counter() - start:.1f} s")
# start A, start B, start C,
# done A, done B, done C, 1.0 s
