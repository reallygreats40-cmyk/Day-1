# Exercise 1: Logging Context Protocol (Scope Warm-up) Template
# Task: Create a class-based context manager named LoggingContext that prints entry and exit logs.

class LoggingContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # TODO: Print entry message and return self
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        # TODO: Print exit message and return False
        pass

# Verification Code
if __name__ == "__main__":
    with LoggingContext("TestBlock"):
        print("Executing code inside block")
