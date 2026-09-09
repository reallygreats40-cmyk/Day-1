"""
Advanced Data Handling & Manipulation
Topic: Lazy Pipelines -- Generators, Iterators and Lazy Evaluation

This is the same underlying pipeline as memory_efficiency.py, shown again
on its own slide to introduce the iterator mechanics that make it work.

"""


def read_numbers(path):
    """Generator: reads numbers line by line without
    holding the whole file in memory. Because it uses `yield`,
    this function satisfies the iterator protocol (__iter__ /
    __next__) automatically -- there is no need to implement
    those methods by hand."""
    with open(path) as f:
        for line in f:
            if line.strip():
                yield int(line.strip())  # one value at a time


def main():
    # Write a dummy numbers file
    with open("numbers.txt", "w") as f:
        f.write("5\n12\n3\n20\n8\n15\n")

    # Generator expression (lazy transformation): a second,
    # chained lazy layer built directly on top of read_numbers
    pipeline = (
        value * 2
        for value in read_numbers("numbers.txt")
        if value > 10
    )
   # print(type(pipeline))
   # print(f' the first value {next(pipeline)}')

    # Values are computed on demand during iteration
    for value in pipeline:
        print(f"Processed: {value}")


if __name__ == "__main__":
    main()
