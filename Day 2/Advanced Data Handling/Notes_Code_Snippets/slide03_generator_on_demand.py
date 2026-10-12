def square(x):
    print(f"  computing {x} * {x}")
    return x * x

def main():
    # Round brackets: a lazy generator
    gen = (square(x) for x in range(1,10, 2))
    print("Generator created: nothing computed yet")

    print(next(gen))     # computes 0 * 0, prints 0
    print(next(gen))     # computes 1 * 1, prints 1
    # The third value is never computed: nobody asked for it

    # Square brackets: a list computes everything at once
    print("Building a list...")
    squares = [square(x) for x in range(1,10,2)]
    print(squares)

if __name__ == "__main__":
    main()
