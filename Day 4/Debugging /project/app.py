def transform(value):
    return str(value).strip().upper()


def process(values):
    output = []
    for value in values:
        output.append(transform(value))
    return output


if __name__ == "__main__":
    values = range(100_000)
    result = process(values)
    print("items:", len(result))
