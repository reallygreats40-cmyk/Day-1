"""
Slide 8: Introduction to asyncio and Coroutines
A basic coroutine that yields control back to the event loop with
asyncio.sleep().
"""
import asyncio


async def greet():
    print("Hello...")
    # Yield control to the loop for 0.5s
    await asyncio.sleep(0.5)
    print("...World!")


async def main():
    # Awaiting suspends main until greet is done
    await greet()
    print('...main is done now ...')


if __name__ == "__main__":
    # Handles event loop lifecycle
    asyncio.run(main())
