# Exercise 7: Dynamic File Handles with ExitStack Solution
# Task: Open a dynamic list of files and write headers to each using contextlib.ExitStack.

from contextlib import ExitStack

def write_headers(file_paths, header_text):
    with ExitStack() as stack:
        handles = [stack.enter_context(open(name, "w")) for name in file_paths]
        for handle in handles:
            handle.write(header_text)
    print(f"[ExitStack] Wrote headers and safely closed {len(file_paths)} files.")

# Verification
if __name__ == "__main__":
    paths = ["file1.txt", "file2.txt", "file3.txt"]
    write_headers(paths, "COLUMN1,COLUMN2,COLUMN3\n")
    
    with open("file1.txt", "r") as f:
        print("File1 content verify:", f.read().strip())
