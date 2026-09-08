"""
Closures Notes Section 1: Namespaces and the LEGB Rule
Demonstrating how Python resolves variables dynamically across different scopes.
"""

# Global scope variable
x = "global_value"

def outer_function():
    # Enclosing (nonlocal) scope variable
    x = "enclosing_value"
    
    def inner_function():
        # Local scope variable
        x = "local_value"
        print(f"Local Scope Resolution: {x}")
        
    inner_function()
    print(f"Enclosing Scope Resolution: {x}")

def main():
    print(f"Global Scope Resolution: {x}")
    outer_function()

if __name__ == "__main__":
    main()
