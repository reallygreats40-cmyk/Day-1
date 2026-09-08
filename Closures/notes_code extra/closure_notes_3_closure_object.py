"""
Closures Notes Section 3: Introspecting Closures and Cell Objects
Demonstrating how closures are physically stored and structured in Python.
"""

def make_power_function(exponent):
    # 'exponent' is the enclosing scope free variable
    def power(base):
        return base ** exponent
    return power

def main():
    square = make_power_function(2)
    cube = make_power_function(3)
    
    # Every closure exposes a '__closure__' tuple containing 'cell' objects
    print("Square closure cells:", square.__closure__)
    print("Cube closure cells:", cube.__closure__)
    
    # We can inspect the actual values stored inside the cell using 'cell_contents'
    if square.__closure__:
        exponent_cell = square.__closure__[0]
        print(f"Square exponent cell contents: {exponent_cell.cell_contents}") # Output: 2
        
    if cube.__closure__:
        exponent_cell = cube.__closure__[0]
        print(f"Cube exponent cell contents: {exponent_cell.cell_contents}") # Output: 3

if __name__ == "__main__":
    main()
