"""
From: "pstats: Filter and Focus the Investigation"

Once a hotspot is known, this reduces how much output there is to read.
Requires profile.prof to already exist (see pstats_save_and_inspect.py).
"""
import pstats

stats = pstats.Stats("profile.prof")

stats.sort_stats("tottime")
stats.print_stats(10)

# Print only entries matching a pattern:
stats.print_stats("transform")

# Inspect callers/callees for a selected function:
stats.print_callers("transform")
stats.print_callees("transform")
