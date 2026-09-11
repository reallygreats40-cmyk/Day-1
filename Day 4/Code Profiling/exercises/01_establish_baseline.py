import time

def workload(n=200_000):
    total = 0

    for i in range(n):
        total += (i * i) % 97

    return total


if __name__ == "__main__":
    start = time.perf_counter()
    result = workload()
    elapsed = time.perf_counter() - start

    print("result:", result)
    print("elapsed:", elapsed)

    # TASK:
    # Repeat the measurement at least five times.
    # Record the typical elapsed time.
    # Do not change the implementation yet.
