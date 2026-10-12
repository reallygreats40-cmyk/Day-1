"""
Slide 4: Synchronizing Threads with a Lock
The same counter as before, now protected by a threading.Lock so the
read-modify-write sequence cannot be interleaved by another thread.
Expected: 200000
Actual: always 200000
"""
import threading
from threading import Thread, Lock
import time

counter = 0
lock = Lock()

# Vector, ArrayList

from getpass import getpass
pw = getpass('enter your password')

def increment():
    global counter
    for _ in range(100000):
        with lock:
            temp = counter        # Read
            time.sleep(0)          # Still forces a switch...
            counter = temp + 1     # ...but the lock blocks the
            # other thread from entering until release


def main():
    threads = [
        Thread(target=increment)
        for _ in range(2)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Counter: {counter}")


if __name__ == "__main__":
    main()
