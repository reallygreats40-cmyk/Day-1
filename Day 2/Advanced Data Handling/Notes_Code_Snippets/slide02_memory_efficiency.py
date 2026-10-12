import sys

def squares_list(n):
    return [x * x for x in range(n)]    # builds every value now

def squares_gen(n):
    return (x * x for x in range(n))    # builds values on request

def main():
    n = 1_000_000
    as_list = squares_list(n)
    as_gen = squares_gen(n)

    # Size of the container object itself
    print(f"List:      {sys.getsizeof(as_list):>10,} bytes")
    print(f"Generator: {sys.getsizeof(as_gen):>10,} bytes")

    # Same answer either way
    print(sum(as_list) == sum(as_gen))  # True

if __name__ == "__main__":
    main()
