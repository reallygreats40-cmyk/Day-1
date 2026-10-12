"""
Exercise 1: Defining and Running a Coroutine
Task: Declare a simple async greeting coroutine and run it using the asyncio loop.
"""
import asyncio


async def async_greet(name):
    print(f"Preparing greeting for {name}...")
    await asyncio.sleep(0.3)
    return f"Welcome, {name} to Async Programming!"


async def main():
    result = await async_greet("Delegate")
    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
