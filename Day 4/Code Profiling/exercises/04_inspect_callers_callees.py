import cProfile
import pstats


def transform(values):
    return [str(v).upper() for v in values]


def process(values):
    output = []

    for v in values:
        output.extend(transform([v]) * 3)

    return output


if __name__ == "__main__":
    values = list(range(20_000))

    profiler = cProfile.Profile()
    profiler.enable()
    process(values)
    profiler.disable()

    profiler.dump_stats("profile.prof")

    stats = pstats.Stats("profile.prof")
    stats.sort_stats("cumulative")

    stats.print_stats(15)
    stats.print_callers("transform")
    stats.print_callees("process")

    # TASK:
    # Identify which caller is responsible for repeated work.
    # Suggest one change that could reduce calls without
    # changing the result.
