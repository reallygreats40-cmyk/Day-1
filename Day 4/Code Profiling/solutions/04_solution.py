import pstats


if __name__ == "__main__":
    stats = pstats.Stats("step3.prof")
    stats.sort_stats("cumulative")

    stats.print_stats(15)
    stats.print_callers("transform")
    stats.print_callees("process")
