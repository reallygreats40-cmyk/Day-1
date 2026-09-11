"""
From: "Copy-and-Paste Template"

Replace workload() with the operation actually being investigated.
Run with: python performance_debug.py
"""
import logging
import time
import tracemalloc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def workload():
    # Replace this with the operation under investigation.
    return sum(i * i for i in range(100_000))


if __name__ == "__main__":
    tracemalloc.start()
    before = tracemalloc.take_snapshot()

    start = time.perf_counter()
    result = workload()
    elapsed = time.perf_counter() - start

    after = tracemalloc.take_snapshot()

    logger.info("elapsed=%.6fs result=%s", elapsed, result)

    for stat in after.compare_to(before, "lineno")[:5]:
        logger.info("memory: %s", stat)

    tracemalloc.stop()
