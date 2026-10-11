"""
Exercise 2: Stateful Multiplier Factory (Capturing Environment)
Objective: Implement a multiplier factory make_multiplier(factor) that creates functions multiplying their input by a closed-over factor.
"""

# Complete the multiplier factory below
def make_multiplier(factor):
    def multiplier(number):
        # TODO: Capture 'factor' to calculate the output
        pass
    return multiplier

# --- Verification ---
if __name__ == "__main__":
    double = make_multiplier(2)
    triple = make_multiplier(3)
    
    print(double(15))  # Expected: 30
    print(triple(15))  # Expected: 45
