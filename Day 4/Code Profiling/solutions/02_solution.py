import time


def workload(n=200_000):
    total = 0

    for i in range(n):
        total += (i * i) % 97

    return total


def benchmark(runs=10):
    times = []

    for _ in range(runs):
        start = time.perf_counter()
        workload()
        times.append(time.perf_counter() - start)

    return times


if __name__ == "__main__":
    times = benchmark()

    print("min:", min(times))
    print("max:", max(times))
    print("avg:", sum(times) / len(times))
