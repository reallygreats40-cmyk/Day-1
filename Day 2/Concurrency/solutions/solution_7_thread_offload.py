"""
Solution 7: Offloading Blocking Synchronous Tasks
Task: Execute a blocking CPU calculation safely in an executor thread without stalling loop steps.
"""
import asyncio
import time


def sync_factorial_calculation(number):
    print(f"Factorial calculation started for {number}...")
    total = 1
    for i in range(1, number + 1):
        total *= i
    time.sleep(1.0)  # Blocking sleep simulating heavy processing calculations
    print(f"Factorial calculation for {number} complete.")
    return total


async def async_reporter():
    for i in range(5):
        print(f"Async reporter ticking: {i}...")
        await asyncio.sleep(0.2)


async def main():
    start = time.perf_counter()

    calc_task = asyncio.create_task(asyncio.to_thread(sync_factorial_calculation, 100))
    report_task = asyncio.create_task(async_reporter())

    await report_task
    result = await calc_task

    elapsed = time.perf_counter() - start
    print(f"Calculation Result: {result}")
    print(f"Concurrent workflow complete in {elapsed:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
