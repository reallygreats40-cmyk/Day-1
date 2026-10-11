"""
Slide 6: Stacking Decorators - Execution Order
Goal: Observe the bottom-up nesting of multiple stacked decorators.
"""

def bold(func):
    """Wraps the function output in HTML bold tags."""
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    """Wraps the function output in HTML italic tags."""
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

# Stacking decorators: bold on top of italic
# Resolves as: greet = bold(italic(greet))
@bold
@italic
def greet():
    return "Hello"

if __name__ == "__main__":
    print("--- Running stacked decorators ---")
    print(f"Output: {greet()}")  # Expected: <b><i>Hello</i></b>
