# Exercise 5: Generator-Based FileManager Template
# Task: Rebuild SafeFileManager using @contextlib.contextmanager.

from contextlib import contextmanager

@contextmanager
def managed_file(path, mode):
    # TODO: Perform setup (open file), yield it, and guarantee cleanup in finally
    pass

# Verification Code
if __name__ == "__main__":
    with managed_file("output2.txt", "w") as f:
        f.write("Safe writing via generator context manager.")
