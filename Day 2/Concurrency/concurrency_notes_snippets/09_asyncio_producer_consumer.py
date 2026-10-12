"""
Slide 12: Asyncio Producer-Consumer Model
asyncio.Queue coordinates a producer coroutine and a background consumer
task. task_done() and q.join() let the producer know when every item
enqueued has actually been processed.
"""
import asyncio

q = asyncio.Queue(maxsize=3)


async def producer():
    for i in range(5):
        await q.put(i)   # Suspends if full
        print(f"Produced: {i}")
        await asyncio.sleep(0.1)


async def consumer():
    while True:
        item = await q.get()   # Suspends if empty
        print(f"Consumed: {item}")
        q.task_done()
        await asyncio.sleep(0.2)


async def main():
    c_task = asyncio.create_task(consumer())
    await producer()
    await q.join()
    c_task.cancel()
    try:
        await c_task
    except asyncio.CancelledError:
        pass
    print("All items processed.")


if __name__ == "__main__":
    asyncio.run(main())
