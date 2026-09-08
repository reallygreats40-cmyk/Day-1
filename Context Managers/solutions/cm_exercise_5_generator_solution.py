# Exercise 5: Generator-Based FileManager Solution
# Task: Rebuild SafeFileManager using @contextlib.contextmanager.

from contextlib import contextmanager

@contextmanager
def managed_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
        print("[Generator FileManager] Resource closed successfully.")

# Verification
if __name__ == "__main__":
    with managed_file("output2.txt", "w") as f:
        f.write("Safe writing via generator context manager.")
        
    with open("output2.txt", "r") as f:
        print("Read verify:", f.read())
