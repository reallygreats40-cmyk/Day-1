def normalise(value):
    return str(value).strip().lower()


def process(values):
    result = []
    for value in values:
        result.append(normalise(value))
    return result


if __name__ == "__main__":
    values = range(200_000)
    result = process(values)
    print(len(result))
