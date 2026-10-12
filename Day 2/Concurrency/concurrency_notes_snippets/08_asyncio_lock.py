"""
Slide 11: Resource Synchronization with Locks
asyncio.Lock ensures only one task can execute the critical section at a
time, even though the await inside it yields control back to the loop.
"""
import asyncio

counter = 0
lock = asyncio.Lock()


async def increment():
    global counter
    async with lock:
        val = counter
        # await yields, but lock blocks others
        await asyncio.sleep(0.01)
        counter = val + 1


async def main():
    await asyncio.gather(*(increment() for _ in range(7)))
    print(f"Counter: {counter}")



if __name__ == "__main__":
    asyncio.run(main())




