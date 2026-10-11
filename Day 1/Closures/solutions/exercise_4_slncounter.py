"""
Exercise 4: Stateful Counter with nonlocal (Modifying State)
Goal: Implement a closure that increments and returns a counter.
"""

def make_counter():
    """
    Returns a function that increments and returns an enclosed count.
    Uses the 'nonlocal' keyword to modify an immutable integer.
    """
    count = 0  # Enclosing variable
    
    def counter():
        nonlocal count  # Required to rebind the outer 'count' variable
        count += 1
        return count
    return counter

# --- Verification ---
if __name__ == "__main__":
    counter_a = make_counter()
    counter_b = make_counter()
    
    print("Counter A:", counter_a())  # Expected: 1
    print("Counter A:", counter_a())  # Expected: 2
    print("Counter B:", counter_b())  # Expected: 1 (isolated state)
    print("Counter A:", counter_a())  # Expected: 3
