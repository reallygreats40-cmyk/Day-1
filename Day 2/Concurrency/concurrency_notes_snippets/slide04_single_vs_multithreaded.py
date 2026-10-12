"""Slide 4: single-threaded vs. multithreaded application.

Three simulated 1-second downloads, first on the main thread only (about 3 s),
then on three threads (about 1 s).
"""

import threading, time

def download(n):
    time.sleep(1)          # waiting on I/O
    print(f"file {n} done")

# Single-threaded: about 3 seconds
start = time.perf_counter()
for n in range(3):
    download(n)
print(f"{time.perf_counter() - start:.1f} s")

# Multithreaded: about 1 second
start = time.perf_counter()
threads = [threading.Thread(target=download,
                            args=(n,))
           for n in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"{time.perf_counter() - start:.1f} s")
