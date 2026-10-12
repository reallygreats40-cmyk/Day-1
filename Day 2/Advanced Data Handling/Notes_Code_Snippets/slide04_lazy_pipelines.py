def read_numbers(path):
    """Generator: yields one number per line, never the whole file."""
    with open(path) as f:
        for line in f:
            if line.strip():
                yield int(line.strip())

def main():
    # Create a small sample file
    with open("numbers.txt", "w") as f:
        f.write("5\n12\n3\n20\n8\n15\n")

    # Generator expression: describes the work, runs nothing yet
    pipeline = (value * 2
                for value in read_numbers("numbers.txt")
                if value > 10)

    # Values are produced one at a time as the loop asks for them
    for value in pipeline:
        print(f"Processed: {value}")    # 24, 40, 30

    # Under the hood: the iterator protocol
    it = iter(read_numbers("numbers.txt"))
    print(next(it), next(it))           # 5 12

if __name__ == "__main__":
    main()
