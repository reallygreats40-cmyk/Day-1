"""
Exercise 2: Stateful Multiplier Factory (Capturing Environment)
Goal: Create a function factory that returns a multiplier function.
"""

def make_multiplier(factor):
    """
    Returns a function that multiplies its input by the enclosed 'factor'.
    """
    def multiplier(number):
        # 'factor' is captured from the enclosing environment
        return number * factor
    return multiplier

# --- Verification ---
if __name__ == "__main__":
    double = make_multiplier(2)
    triple = make_multiplier(3)
    
    print(double(15))  # Expected: 30
    print(triple(15))  # Expected: 45
