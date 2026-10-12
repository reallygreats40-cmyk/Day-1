"""
Slide 1: Multithreading in Python
Spawning a real OS-level thread and waiting for it to finish with join().
"""
import threading
import time


def worker():
    print("Thread started")
    time.sleep(0.5)
    print("Thread done")


def main():
    # Create thread object
    t = threading.Thread(target=worker)
    # Start the thread execution
    t.start()
    # Block main thread until t completes
    t.join()
    print("Main finished.")


if __name__ == "__main__":
    main()
