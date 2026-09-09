"""
Solution 4: Bounded Web Requests with Timeouts
Task: Apply a strict timeout boundary to a lagging query, handling errors gracefully.
"""
import asyncio


async def download_heavy_archive():
    print("Beginning massive archive download stream...")
    await asyncio.sleep(2.5)  # Simulate network drag
    return "ARCHIVE_BYTES"


async def main():
    try:
        data = await asyncio.wait_for(download_heavy_archive(), timeout=1.0)
        print(f"Success: {data}")
    except asyncio.TimeoutError:
        print("Network boundary exceeded! Download timed out. Falling back to local mirror.")


if __name__ == "__main__":
    asyncio.run(main())
