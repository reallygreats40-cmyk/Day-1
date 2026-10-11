# Slide 10: Avoid two common context manager mistakes

# Risky: file opened before __enter__ even runs
class RiskyFile:
    def __init__(self, path):
        self.f = open(path, 'w')

    def __enter__(self):
        return self.f

    def __exit__(self, *exc):
        self.f.close()


# Safer: acquisition tied to the with block
class SaferFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.f = open(self.path, 'w')
        return self.f

    def __exit__(self, *exc):
        self.f.close()
        return False  # never swallow errors


if __name__ == "__main__":
    with RiskyFile('risky.txt') as f:
        f.write('written via RiskyFile')

    with SaferFile('safer.txt') as f:
        f.write('written via SaferFile')

    print("Both files written successfully.")

# Design insight:
# If constructing RiskyFile raises after opening the file,
# the with block never starts, so __exit__ never runs to close it.
