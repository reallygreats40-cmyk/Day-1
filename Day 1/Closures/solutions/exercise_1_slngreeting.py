"""
Exercise 1: Basic Greeting Closure (Scope Warm-up)
Goal: Create a closure that generates custom greeting functions with a fixed prefix.
"""

def make_greeter(prefix):
    """
    An outer function acting as a closure factory.
    It takes a prefix and returns a function that applies it.
    """
    def greeter(name):
        # prefix is captured from the enclosing scope of make_greeter
        return f"{prefix}, {name}!"
    return greeter

# --- Verification ---
if __name__ == "__main__":
    welcome_greet = make_greeter("Welcome")
    formal_greet = make_greeter("Good morning")
    
    print(welcome_greet("Alice"))  # Expected: Welcome, Alice!
    print(formal_greet("Bob"))    # Expected: Good morning, Bob!
