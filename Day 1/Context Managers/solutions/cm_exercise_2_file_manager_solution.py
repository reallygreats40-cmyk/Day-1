# Exercise 2: Safe File Manager Class (Resource Safety) Solution
# Task: Implement a class-based context manager named SafeFileManager that guarantees file closures.

class SafeFileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        if self.file:
            self.file.close()
        return False # Let exceptions propagate

# Verification
if __name__ == "__main__":
    with SafeFileManager("output.txt", "w") as f:
        f.write("Safe writing via custom FileManager class.")
    
    with open("output.txt", "r") as f:
        print("Read verify:", f.read())
