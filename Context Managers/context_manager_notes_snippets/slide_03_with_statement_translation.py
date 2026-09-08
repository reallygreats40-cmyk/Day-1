# Slide 3: The with statement calls __enter__ and __exit__ for you

# Set up a sample file to work with
with open('data.txt', 'w') as _setup:
    _setup.write('placeholder\n')

# What you write:
with open('data.txt', 'w') as f:
    f.write('hello')

# What Python actually does, translated manually:
f_ctx = open('data.txt', 'w')
f = f_ctx.__enter__()
try:
    f.write('hello')
except BaseException as exc:
    if not f_ctx.__exit__(type(exc), exc, exc.__traceback__):
        raise
else:
    f_ctx.__exit__(None, None, None)

# Design insight:
# A file object already implements __enter__ and __exit__,
# so open() can be used directly after the with keyword.

if __name__ == "__main__":
    with open('data.txt') as f:
        print(f"File contents: {f.read()}")  # -> 'hello'
