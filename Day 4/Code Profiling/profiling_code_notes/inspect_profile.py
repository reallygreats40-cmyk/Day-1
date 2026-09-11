"""
From: "pstats: Save and Inspect a Profile Offline"

First create profile.prof with:
    python -m cProfile -o profile.prof app.py

Then run this file to analyse it without rerunning the application.
"""
import pstats

stats = pstats.Stats("profile.prof")

stats.sort_stats("cumulative")
stats.print_stats(20)

print("\n--- CALLERS ---")
stats.print_callers("transform") #  who calls transform?

print("\n--- CALLEES ---")
stats.print_callees("process") # what does process call?
