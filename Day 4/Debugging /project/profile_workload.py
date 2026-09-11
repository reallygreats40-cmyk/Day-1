import cProfile
import pstats


def workload():
    # Replace this with the operation you want to investigate.
    values = range(100_000)
    return sum(x * x for x in values)


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    result = workload()
    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    stats.print_stats(20)
    print("result:", result)
