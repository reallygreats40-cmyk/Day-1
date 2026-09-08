"""
Exercise 4: Stateful Counter with nonlocal (Modifying State)
Objective: Build a function make_counter() that implements an isolated stateful counter incremented on each call.
"""

def make_counter():
    count = 0
    
    def counter():
        # TODO: Increment and return the outer count variable
        pass
    return counter

# --- Verification ---
if __name__ == "__main__":
    counter_a = make_counter()
    
    print(counter_a())  # Expected: 1
    print(counter_a())  # Expected: 2
