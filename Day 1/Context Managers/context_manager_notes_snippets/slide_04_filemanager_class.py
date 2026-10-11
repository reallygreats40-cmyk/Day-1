# Slide 4: Dunder methods define the context lifecycle

class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, tb):
        self.file.close()
        return False  # propagate exceptions


# Usage
if __name__ == "__main__":
    with FileManager('notes.txt', 'w') as f:
        f.write('logged safely\n')

    with FileManager('notes.txt', 'r') as f:
        print(f"Contents: {f.read()!r}")

# Design insight:
# FileManager is a plain class. There is no magic beyond
# Python calling __enter__ and __exit__ at the right times.
