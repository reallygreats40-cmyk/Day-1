"""
Solution 6: Throttling Concurrency with Semaphores
Task: Throttle 5 concurrent operations so that at most 2 run in parallel.
"""
import asyncio
import time

api_semaphore = asyncio.Semaphore(2)


async def call_restricted_api(client_id):
    async with api_semaphore:
        print(f"Client {client_id} calling limited endpoint...")
        await asyncio.sleep(0.4)
        print(f"Client {client_id} request complete.")


async def main():
    start = time.perf_counter()
    await asyncio.gather(*(call_restricted_api(i) for i in range(5)))
    elapsed = time.perf_counter() - start
    print(f"Throttled execution complete in {elapsed:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
