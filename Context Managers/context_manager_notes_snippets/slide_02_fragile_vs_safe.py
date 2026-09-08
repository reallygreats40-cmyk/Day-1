# Slide 2: Resources demand deterministic cleanup at the call site
# Fragile vs. safe file cleanup patterns

# Fragile: close() is skipped if process() raises
def process(f):
    """Placeholder for whatever work you do with the file."""
    print(f"Processing contents of {f.name}")


# Set up a sample file to work with
with open('data.txt', 'w') as _setup:
    _setup.write('sample content\n')

f = open('data.txt')
try:
    process(f)
finally:
    f.close()

# Safe and idiomatic: cleanup is guaranteed
with open('data.txt') as f:
    process(f)

# Design insight:
# A with block guarantees f.close() runs on the way out,
# whether process(f) succeeds, fails, or returns early.
