"""
Exercise 6: Memoization Cache (Advanced Closures)
Objective: Build a caching closure make_cached(func) that wraps an expensive function and stores previously computed arguments in a dictionary cache.
"""

def make_cached(func):
    cache = {}
    
    def cached_wrapper(x):
        # TODO: Check cache, calculate if missing, return cached result
        pass
    return cached_wrapper

# --- Verification ---
if __name__ == "__main__":
    def slow_square(x): 
        return x * x
        
    memo_square = make_cached(slow_square)
    
    print(memo_square(4))  # Expected: Cache Miss & 16
    print(memo_square(4))  # Expected: Cache Hit & 16
