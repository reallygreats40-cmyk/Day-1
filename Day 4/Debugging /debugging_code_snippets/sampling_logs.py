"""
From: "Sampling Logs in a Hot Loop"

Only 10 progress messages are emitted across all 100,000 iterations.
Run with: python sampling_logs.py
"""
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    for index, value in enumerate(range(100_000)):
        if index % 10_000 == 0:
            logger.debug(
                "progress index=%d value=%d",
                index, value,
            )

        # application work
