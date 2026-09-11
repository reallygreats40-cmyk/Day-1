"""
From: "faulthandler for Difficult Runtime Problems"

Run with: python faulthandler_demo.py
"""
import faulthandler
import time
import sys

faulthandler.enable()

# Arm a watchdog: if the program is still running 2 seconds from now,
# dump every thread's current stack to stderr. Since sleep(3) below
# takes longer than that, this will fire while we're still sleeping.
faulthandler.dump_traceback_later(2, exit=False, file=sys.stderr)

if __name__ == "__main__":
    print("Program started")

    # Simulate a long-running operation
    time.sleep(3)

    print("Program finished")

    # Cancel the watchdog since we finished normally — otherwise it
    # stays armed for the rest of the process's lifetime.
    faulthandler.cancel_dump_traceback_later()
