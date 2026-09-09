"""
Advanced Data Handling & Manipulation
Topic: Memory Efficiency -- Why Advanced Data Handling Matters

Run this file directly to see the output: python memory_efficiency.py
"""


def read_numbers(path):
    """Generator: reads numbers line by line without
    holding the whole file in memory."""
    with open(path) as f:
        for line in f:
            if line.strip():
                yield int(line.strip())


def main():
    # Write a dummy numbers file
    with open("numbers.txt", "w") as f:
        f.write("5\n12\n3\n20\n8\n15\n")

    # Generator expression (lazy transformation) --
    # nothing runs yet, this just describes the pipeline
    pipeline = (
        value * 2
        for value in read_numbers("numbers.txt")
        if value > 10
    )

    # Values are computed on demand during iteration
    for value in pipeline:
        print(f"Processed: {value}")


if __name__ == "__main__":
    main()
