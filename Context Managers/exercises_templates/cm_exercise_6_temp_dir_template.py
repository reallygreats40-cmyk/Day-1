# Exercise 6: Isolated Temporary Workspace Template
# Task: Create a context manager named temp_workspace that yields a pathlib.Path workspace folder.

import shutil
from pathlib import Path
from tempfile import mkdtemp
from contextlib import contextmanager

@contextmanager
def temp_workspace():
    # TODO: Create temporary directory, yield Path object, delete folder recursively on exit
    pass

# Verification Code
if __name__ == "__main__":
    with temp_workspace() as ws:
        test_file = ws / "test.txt"
        test_file.write_text("Hello workspace")
        print("Workspace path:", ws)
        print("Exists inside block:", test_file.exists())
