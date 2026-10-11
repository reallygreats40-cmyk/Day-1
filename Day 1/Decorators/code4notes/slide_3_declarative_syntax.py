"""
Slide 3: Declarative Wrappers - The @ Syntax
Goal: Understand how the '@' symbol acts as compiler sugar for functional reassignment.
"""

def logged(func):
    """
    A decorator wrapper that logs execution bounds.
    """
    def wrapper():
        print(f"Invoking: {func.__name__}")
        func()
    return wrapper

# Syntactic sugar equivalent to: greet = logged(greet)
@logged
def greet():
    print("Greetings, delegates!")

if __name__ == "__main__":
    print("--- Running decorated greet() ---")
    greet()  # Automatically logs its invocation!
