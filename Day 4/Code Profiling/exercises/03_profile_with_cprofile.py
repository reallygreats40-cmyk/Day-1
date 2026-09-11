import cProfile
import pstats


def transform(values):
    return [str(v).upper() for v in values]


def process(values):
    output = []

    for v in values:
        # Deliberately repeated work
        output.extend(transform([v]) * 3)

    return output


if __name__ == "__main__":
    values = list(range(20_000))

    profiler = cProfile.Profile()
    profiler.enable()

    process(values)

    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats("cumulative")
    stats.print_stats(10)

    # TASK:
    # Identify the top three functions.
    # Explain ncalls, tottime and cumtime.
