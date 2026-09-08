"""
Closures Notes Section 4: The nonlocal Keyword and Enclosing State Reassignment
Demonstrating how to modify variables in the enclosing scope safely.
"""

def make_counter_broken():
    count = 0
    def counter():
        # Attempting to reassign an enclosing variable directly raises an UnboundLocalError
        # because Python treats any local assignment as a local variable declaration.
        # Uncommenting the line below will crash!
        # count += 1 
        return count
    return counter

def make_counter_working():
    count = 0
    def counter():
        # The 'nonlocal' keyword tells Python to look in the enclosing scope
        # rather than creating a new local variable during assignment.
        nonlocal count
        count += 1
        return count
    return counter

def main():
    counter = make_counter_working()
    print("Counter call 1:", counter())  # Output: 1
    print("Counter call 2:", counter())  # Output: 2
    print("Counter call 3:", counter())  # Output: 3

if __name__ == "__main__":
    main()
