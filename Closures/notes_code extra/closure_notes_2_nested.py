"""
Closures Notes Section 2: Nested Functions and Lexical Scoping
Demonstrating how inner functions capture outer enclosing scopes.
"""

def make_greeter(greeting):
    # This outer enclosing function defines a variable
    def greet(name):
        # The inner function accesses 'greeting' from its lexical scope
        return f"{greeting}, {name}!"
    return greet

def main():
    # 'make_greeter' executes and returns the inner 'greet' function
    say_hello = make_greeter("Hello")
    say_hola = make_greeter("Hola")
    
    # Even though 'make_greeter' has finished running, the returned function
    # still retains access to its enclosing 'greeting' value!
    print(say_hello("Alice"))  # Output: Hello, Alice!
    print(say_hola("Bob"))     # Output: Hola, Bob!

if __name__ == "__main__":
    main()
