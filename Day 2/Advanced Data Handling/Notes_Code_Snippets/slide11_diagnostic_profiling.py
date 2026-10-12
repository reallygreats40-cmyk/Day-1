import tracemalloc

def build_list():
    return [x * 2 for x in range(500_000)]       # whole list in memory

def generator_sum():
    return sum(x * 2 for x in range(500_000))    # one value at a time

def peak_mb(func):
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / (1024 * 1024)

def main():
    print(f"List peak:      {peak_mb(build_list):.2f} MB")
    print(f"Generator peak: {peak_mb(generator_sum):.3f} MB")

if __name__ == "__main__":
    main()
