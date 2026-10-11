# Exercise 1: Logging Context Protocol (Scope Warm-up) Solution
# Task: Create a class-based context manager named LoggingContext that prints entry and exit logs.

class LoggingContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"[LoggingContext] Entering block: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        print(f"[LoggingContext] Exiting block: {self.name}")
        if exc_type:
            print(f"[LoggingContext] Exception handled: {exc_val}")
        return False # Let exceptions propagate

# Verification
if __name__ == "__main__":
    with LoggingContext("TestBlock"):
        print("Executing code inside block")
