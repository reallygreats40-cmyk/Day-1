# Exercise 7: Dynamic File Handles with ExitStack Template
# Task: Open a dynamic list of files and write headers to each using contextlib.ExitStack.

from contextlib import ExitStack

def write_headers(file_paths, header_text):
    # TODO: Open all paths dynamically using ExitStack, write header_text
    pass

# Verification Code
if __name__ == "__main__":
    paths = ["file1.txt", "file2.txt", "file3.txt"]
    write_headers(paths, "COLUMN1,COLUMN2,COLUMN3\n")
