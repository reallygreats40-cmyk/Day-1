import cProfile
import pstats

from app import process

values = range(100_000)

profiler = cProfile.Profile()
profiler.enable()
process(values)
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(15)
