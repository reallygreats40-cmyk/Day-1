"""
Exercise 2: Concurrent Task Scheduling
Task: Wrap multiple instances of a slow coroutine in background Tasks to execute in parallel.
"""
import asyncio
import time


async def fetch_api_endpoint(endpoint, delay):
    print(f"Polling {endpoint}...")
    await asyncio.sleep(delay)
    print(f"Polled {endpoint} successfully.")
    return f"{endpoint}_data"


async def main():
    start = time.perf_counter()

    task1 = asyncio.create_task(fetch_api_endpoint("/users", 0.5))
    task2 = asyncio.create_task(fetch_api_endpoint("/products", 0.2))
    task3 = asyncio.create_task(fetch_api_endpoint("/metrics", 0.4))

    r1, r2, r3 = await task1, await task2, await task3

    elapsed = time.perf_counter() - start
    print(f"Results: {r1}, {r2}, {r3}")
    print(f"Completed in {elapsed:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
