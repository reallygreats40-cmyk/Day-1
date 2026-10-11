# Exercise 2: Safe File Manager Class (Resource Safety) Template
# Task: Implement a class-based context manager named SafeFileManager that guarantees file closures.

class SafeFileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        # TODO: Open file and return file handle
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        # TODO: Guarantee file closure
        pass

# Verification Code
if __name__ == "__main__":
    with SafeFileManager("output.txt", "w") as f:
        f.write("Safe writing via custom FileManager class.")
