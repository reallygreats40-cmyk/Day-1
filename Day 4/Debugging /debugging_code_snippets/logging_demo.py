"""
From: "Structured Logging for Performance Diagnosis"

Run with: python logging_demo.py
"""
import logging
import time

# Configure the root logging behavior: minimum severity level to show,
# and the format each log line will be printed in
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s",
    filename="app.log",   # writes here instead of the console
    filemode="w",         # "w" = overwrite each run, "a" = append (default)
)
logger = logging.getLogger(__name__)  # a logger scoped to this module's name


def process(values):
    start = time.perf_counter()                     # high-resolution start timestamp
    result = [value * 2 for value in values]         # the actual workload being timed
    elapsed = time.perf_counter() - start             # time taken, in seconds

    logger.info(
        "process items=%d elapsed=%.6fs",     # %-style placeholders, filled in below
        len(values), elapsed,     # deferred formatting: only built if INFO is enabled
    )
    return result


if __name__ == "__main__":
    process(range(100_000))