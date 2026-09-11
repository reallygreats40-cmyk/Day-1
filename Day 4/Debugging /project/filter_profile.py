import cProfile
import os
import pstats

from app import process

PROFILE_PATH = "profile.prof"

if not os.path.exists(PROFILE_PATH):
    # Generate the profile file if it does not exist yet, so this
    # script can be run standalone without a separate profiling step.
    profiler = cProfile.Profile()
    profiler.enable()
    process(range(100_000))
    profiler.disable()
    profiler.dump_stats(PROFILE_PATH)

stats = pstats.Stats(PROFILE_PATH)
stats.sort_stats("tottime")
stats.print_stats(10)

# Print only entries matching a pattern:
stats.print_stats("transform")

# Inspect callers/callees for one function:
stats.print_callers("transform")
stats.print_callees("transform")
