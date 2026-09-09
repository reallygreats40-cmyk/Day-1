"""
Slide 10: Orchestrating with asyncio.gather
gather() runs multiple coroutines concurrently and returns their results in
the same order they were passed in, regardless of completion order.
"""
import asyncio


async def process(val):
    await asyncio.sleep(0.1)
    return val * 10


async def main():
    # Run multiple coroutines concurrently
    results = await asyncio.gather(
        process(1),
        process(2),
        process(3)
    )
    # Guaranteed returned in call order
    print(f"Gathered results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
