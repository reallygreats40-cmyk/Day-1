import time

def workload(n=200_000):
    total = 0

    for i in range(n):
        total += (i * i) % 97

    return total


if __name__ == "__main__":
    times = []

    for _ in range(10):
        start = time.perf_counter()
        workload()
        times.append(time.perf_counter() - start)

    print("min:", min(times))
    print("max:", max(times))
    print("avg:", sum(times) / len(times))

    # TASK:
    # Explain why a single timing is unreliable.
    # Consider system load and other sources of measurement noise.
