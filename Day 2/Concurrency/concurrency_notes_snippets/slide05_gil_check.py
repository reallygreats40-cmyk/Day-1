"""Slide 5: checking whether the Global Interpreter Lock (GIL) is enabled.

Requires Python 3.13 or later.
"""

import sys
# Python 3.13 or later
print(sys._is_gil_enabled())
# True  on the standard build (GIL on)
# False on a free-threaded build,
#       for example python3.15t
