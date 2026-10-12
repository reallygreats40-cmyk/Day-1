"""
Exercise 1: Generators, Iterators and Lazy Evaluation
Task: Refactor a list loader into a lazy streaming pipeline.
"""
# Baseline list-based data loader (materializes everything)
def load_all_records_baseline(data_list):
    results = []
    for item in data_list:
        # Simulate processing and filtering
        if item > 0:
            results.append(item * 10)
    return results

# TODO: Refactor the code above into a lazy generator function
def stream_records_lazy(data_list):
    """
    Yields processed numbers one at a time, lazily.
    """
    # Implement lazy evaluation using yield here
    pass

# Verification
if __name__ == "__main__":
    raw_data = [5, -2, 12, 0, 8, -1]
    baseline_out = load_all_records_baseline(raw_data)
    print(f"Baseline Output (List): {baseline_out}")
    lazy_gen = stream_records_lazy(raw_data)
    print(f"Is generator: {hasattr(lazy_gen, '__next__')}")
    if lazy_gen is not None:
        try:
            print(f"Lazy Output (Stream): {list(lazy_gen)}")
        except Exception as e:
            print(f"Error executing lazy generator: {e}")
