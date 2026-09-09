"""
Slide 9: Concurrency with asyncio.create_task
create_task() schedules a coroutine to start running immediately, so two
fetches launched upfront finish in parallel rather than one after another.
"""
import asyncio


async def fetch(id_code):
    print(f"Start fetch {id_code}...")
    await asyncio.sleep(0.5)
    print(f"End fetch {id_code}")
    return f"Data {id_code}"


async def main():
    # Schedule concurrently on the active loop
    t1 = asyncio.create_task(fetch("A"))
    t2 = asyncio.create_task(fetch("B"))
    # Await in parallel
    res1 = await t1
    res2 = await t2
    print(f"Results: {res1}, {res2}")


if __name__ == "__main__":
    asyncio.run(main())
