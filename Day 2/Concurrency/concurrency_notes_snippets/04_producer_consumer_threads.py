"""
Slide 6: Producer-Consumer with Threads
A bounded queue.Queue coordinates a producer and consumer thread. A None
sentinel signals the consumer that no more work is coming.
"""
import queue
import threading
import time

q = queue.Queue(maxsize=3)


def producer():
    for i in range(5):
        print(f"Producing: {i}")
        q.put(i)   # Blocks if full
        time.sleep(0.1)
    q.put(None)     # Sentinel


def consumer():
    while True:
        item = q.get()   # Blocks if empty
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(0.2)


def main():
    p = threading.Thread(target=producer)
    c = threading.Thread(target=consumer)
    p.start()
    c.start()
    p.join()
    c.join()


if __name__ == "__main__":
    main()
