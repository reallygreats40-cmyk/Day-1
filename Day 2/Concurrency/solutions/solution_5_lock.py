"""
Solution 5: State Synchronization with Lock
Task: Safeguard a concurrent shared metrics dict from race conditions using a Lock.
"""
import asyncio

shared_metrics = {"page_views": 0}
metrics_lock = asyncio.Lock()


async def record_page_view(user_id):
    global shared_metrics
    print(f"User {user_id} browsing page...")
    async with metrics_lock:
        current = shared_metrics["page_views"]
        await asyncio.sleep(0.05)  # Intercept and force context switch
        shared_metrics["page_views"] = current + 1


async def main():
    await asyncio.gather(*(record_page_view(i) for i in range(10)))
    print(f"Expected page views: 10 | Actual recorded views: {shared_metrics['page_views']}")


if __name__ == "__main__":
    asyncio.run(main())
