import cProfile
import os
import pstats

from app import process

PROFILE_PATH = "profile.prof"

if not os.path.exists(PROFILE_PATH):
    # Generate the profile file if it does not exist yet, so this
    # script can be run standalone without a separate profiling step.
    # (In the walkthrough this is created with:
    #    python -m cProfile -o profile.prof app.py)
    profiler = cProfile.Profile()
    profiler.enable()
    process(range(100_000))
    profiler.disable()
    profiler.dump_stats(PROFILE_PATH)

stats = pstats.Stats(PROFILE_PATH)
stats.sort_stats("cumulative")
stats.print_stats(20)

print("\n--- CALLERS ---")
stats.print_callers("transform")

print("\n--- CALLEES ---")
stats.print_callees("process")
