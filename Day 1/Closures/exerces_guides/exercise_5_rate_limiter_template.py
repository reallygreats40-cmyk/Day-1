"""
Exercise 5: API Rate Limiter (Real-world Utility)
Objective: Write a rate limiter closure make_rate_limiter(max_calls) that restricts function calls, printing a warning and refusing execution once the threshold is crossed.
"""

def make_rate_limiter(max_calls):
    calls_made = 0
    
    def rate_limiter(func, *args, **kwargs):
        # TODO: Track count, block execution if calls_made >= max_calls
        pass
    return rate_limiter

# --- Verification ---
if __name__ == "__main__":
    def get_data(): 
        return "Data"
        
    limiter = make_rate_limiter(2)
    
    print(limiter(get_data))  # Expected: "Data"
    print(limiter(get_data))  # Expected: "Data"
    print(limiter(get_data))  # Expected: WARNING printed & None returned
