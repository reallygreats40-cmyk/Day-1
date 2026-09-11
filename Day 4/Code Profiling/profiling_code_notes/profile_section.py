"""
From: "cProfile From Inside Python"

Profiles only the workload of interest, rather than the whole program.
Run with: python profile_section.py
"""
import cProfile
import pstats

from sympy import factorial

from app import process

values = range(100_000)

profiler = cProfile.Profile()
profiler.enable()

process(values)

profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(15)

