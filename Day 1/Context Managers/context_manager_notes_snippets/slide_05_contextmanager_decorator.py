# Slide 5: The @contextmanager decorator simplifies linear lifecycles

from contextlib import contextmanager


@contextmanager
def managed_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()  # guaranteed cleanup


# Usage
if __name__ == "__main__":
    with managed_file('log.txt', 'w') as f:
        f.write('entry\n')

    with managed_file('log.txt', 'r') as f:
        print(f"Log contents: {f.read()}")

# Design insight:
# Without try/finally, an exception inside the with block
# would skip f.close() and leak the open file handle.
