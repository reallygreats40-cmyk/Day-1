# Exercise 6: Isolated Temporary Workspace Solution
# Task: Create a context manager named temp_workspace that yields a pathlib.Path workspace folder.

import shutil
from pathlib import Path
from tempfile import mkdtemp
from contextlib import contextmanager

@contextmanager
def temp_workspace():
    raw_path = mkdtemp()
    ws_path = Path(raw_path)
    try:
        yield ws_path
    finally:
        shutil.rmtree(raw_path)
        print(f"[Workspace Cleanup] Deleted folder recursively: {raw_path}")

# Verification
if __name__ == "__main__":
    with temp_workspace() as ws:
        test_file = ws / "test.txt"
        test_file.write_text("Hello workspace")
        print("Workspace path:", ws)
        print("Exists inside block:", test_file.exists())
    
    print("Folder exists after cleanup:", ws.exists())
