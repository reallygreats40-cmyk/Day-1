"""
Exercise 5: API Rate Limiter (Real-world Utility)
Goal: Implement a simple rate limiter closure that restricts function calls.
"""

def make_rate_limiter(max_calls):
    """
    Returns a function wrapper that allows execution up to max_calls.
    Subsequent calls are blocked with a warning message.
    """
    calls_made = 0
    
    def rate_limiter(func, *args, **kwargs):
        nonlocal calls_made
        if calls_made < max_calls:
            calls_made += 1
            return func(*args, **kwargs)
        else:
            print("WARNING: Rate limit exceeded! Request blocked.")
            return None
    return rate_limiter

# --- Verification ---
if __name__ == "__main__":
    def get_data():
        return "Prisitine API Data"
        
    limiter = make_rate_limiter(2)
    
    print(limiter(get_data))  # Expected: Prisitine API Data
    print(limiter(get_data))  # Expected: Prisitine API Data
    print(limiter(get_data))  # Expected: WARNING + None
