"""
Solution 8: Capstone - Producer-Consumer Pipeline with Semaphore Rate-Limiter
Task: Build an end-to-end asynchronous pipeline where producers generate raw API payloads,
an asyncio.Queue pools them, and consumers process them under a Semaphore rate limit.
"""
import asyncio

# Rate limit: max 2 active processing tasks concurrently
process_semaphore = asyncio.Semaphore(2)


async def raw_data_producer(queue, batch_size):
    for i in range(1, batch_size + 1):
        await asyncio.sleep(0.05)  # Simulate payload ingestion
        payload = f"raw_record_{i}"
        print(f"Producer pushed {payload} into queue.")
        await queue.put(payload)
    print("Producer has completed ingestion.")


async def raw_data_consumer(queue):
    while True:
        item = await queue.get()
        async with process_semaphore:
            print(f"Consumer started parsing {item}...")
            await asyncio.sleep(0.2)  # Simulate work
            print(f"Consumer finished parsing {item}.")
        queue.task_done()


async def main():
    pipeline_queue = asyncio.Queue(maxsize=3)

    consumer_task = asyncio.create_task(raw_data_consumer(pipeline_queue))

    await raw_data_producer(pipeline_queue, 6)

    await pipeline_queue.join()
    print("Pipeline work has converged. Shutting down consumer background loop.")
    if consumer_task:
        consumer_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
