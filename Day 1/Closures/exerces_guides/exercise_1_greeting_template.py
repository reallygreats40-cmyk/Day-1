"""
Exercise 1: Basic Greeting Closure (Scope Warm-up)
Objective: Build a closure factory make_greeter(prefix) that generates customized greeting functions.
"""

# Complete the factory function below
def make_greeter(prefix):
    def greeter(name):
        # TODO: Return the formatted greeting using prefix and name
        pass
    return greeter

# --- Verification ---
if __name__ == "__main__":
    welcome_greet = make_greeter("Welcome")
    formal_greet = make_greeter("Good morning")
    
    print(welcome_greet("Alice"))  # Expected: "Welcome, Alice!"
    print(formal_greet("Bob"))    # Expected: "Good morning, Bob!"
