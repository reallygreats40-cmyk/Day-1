"""
Slide 3: Race Conditions and Thread Safety
Two threads increment an unprotected shared counter. A forced context switch
(time.sleep(0)) makes the lost updates reproducible on every run.
Expected: 200000
Actual: reliably less
"""
import threading
import time

counter = 0


def increment():
    global counter
    for _ in range(100000):
        temp = counter      # Read
        time.sleep(0)        # Force a context switch here
        counter = temp + 1   # Write


def main():
    threads = [
        threading.Thread(target=increment)
        for _ in range(2)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Counter: {counter}")


if __name__ == "__main__":
    main()
