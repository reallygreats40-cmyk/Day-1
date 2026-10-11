"""
Slide 7: Decorators with Arguments - Decorator Factories
Goal: Construct a three-tier architecture to customize decorator behavior at definition time.
"""
from functools import wraps

def repeat(num_times):  # Tier 1: Factory (receives custom configurations)
    """
    A decorator factory that generates a customized repetition decorator.
    """
    def decorator_repeat(func):  # Tier 2: Decorator (receives target function)
        @wraps(func)
        def wrapper(*args, **kwargs):  # Tier 3: Wrapper (intercepts execution)
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

# The factory repeat(num_times=3) runs first, returning a custom decorator_repeat
@repeat(num_times=3)
def hello(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    print("--- Running hello() with repetition parameter ---")
    hello("Bob")  # Expected to repeat 3 times
