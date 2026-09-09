"""
Solution 3: Bulk Gathering of Awaitables
Task: Use asyncio.gather to aggregate dynamic counts of concurrent API queries.
"""
import asyncio


async def fetch_product_inventory(product_id):
    print(f"Fetching stock levels for ID: {product_id}...")
    await asyncio.sleep(0.3)
    return {product_id: 10 + (product_id % 5)}


async def main():
    product_ids = [101, 102, 103, 104, 105]

    results = await asyncio.gather(
        *(fetch_product_inventory(pid) for pid in product_ids)
    )

    print(f"Gathered inventory counts: {results}")


if __name__ == "__main__":
    asyncio.run(main())
