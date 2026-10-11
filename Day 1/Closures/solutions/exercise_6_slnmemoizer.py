"""
Exercise 6: Memoization Cache (Advanced Closures)
Goal: Build a cache decorator-like closure to avoid redundant computations.
"""

def make_cached(func):
    """
    Returns a function that wraps 'func', storing inputs and outputs in an enclosed dictionary.
    """
    cache = {}  # Enclosing dictionary for storing results
    
    def cached_wrapper(x):
        if x not in cache:
            print(f"[CACHE MISS] Calculating result for {x}...")
            cache[x] = func(x)
        else:
            print(f"[CACHE HIT] Retrieving cached result for {x}...")
        return cache[x]
    return cached_wrapper

# --- Verification ---
if __name__ == "__main__":
    def expensive_square(x):
        return x * x
        
    memo_square = make_cached(expensive_square)
    
    print(memo_square(4))  # Expected: Cache Miss, 16
    print(memo_square(4))  # Expected: Cache Hit, 16
    print(memo_square(5))  # Expected: Cache Miss, 25
