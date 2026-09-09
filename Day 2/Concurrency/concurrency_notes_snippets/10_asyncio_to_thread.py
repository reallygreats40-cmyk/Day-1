"""
Slide 13: Integrating Synchronous Blocking Code
asyncio.to_thread() offloads a blocking synchronous call to a worker thread
so it does not stall the event loop.
"""
import asyncio
import time


def blocking_write(data):
    # Simulate a blocking synchronous disk write
    print(f"Starting write for {data}...")
    time.sleep(0.5)
    print(f"Finished write for {data}")
    return f"Saved {data}"


async def main():
    # Offload the blocking function safely
    result = await asyncio.to_thread(
        blocking_write, "dataset_v6"
    )
    print(f"Outcome: {result}")


if __name__ == "__main__":
    asyncio.run(main())
