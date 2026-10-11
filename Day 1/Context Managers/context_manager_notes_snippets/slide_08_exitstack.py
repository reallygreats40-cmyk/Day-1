# Slide 8: ExitStack manages a variable number of resources

from contextlib import ExitStack

filenames = ['a.txt', 'b.txt', 'c.txt']

with ExitStack() as stack:
    handles = [
        stack.enter_context(open(name, 'w'))
        for name in filenames
    ]
    for handle in handles:
        handle.write('managed safely')

# All three files are closed here,
# even if one of the writes had failed.

if __name__ == "__main__":
    for name in filenames:
        with open(name) as f:
            print(f"{name}: {f.read()}")

# Design insight:
# Batch file writers, multi-database routers, and network
# socket pools all rely on this dynamic registration pattern.
