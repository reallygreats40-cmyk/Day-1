"""
Exercise 2: itertools for Efficient Data Pipelines
Task: Process records with itertools, not intermediate lists.
"""
from itertools import islice, groupby, accumulate

# TODO: Refactor this list-based processor using itertools
def process_data_pipeline_baseline(raw_records):
    sorted_records = sorted(
        raw_records, key=lambda x: x["category"])
    grouped_totals = {}
    for key, group in groupby(
            sorted_records, key=lambda x: x["category"]):
        group_list = list(group)
        slice_items = group_list[:3]
        total_sum = sum(item["val"] for item in slice_items)
        grouped_totals[key] = total_sum
    return grouped_totals

# TODO: Build a lazy transformation stream using islice and groupby
def process_data_pipeline_itertools(raw_records):
    """
    Sorts, groups, slices first 3 elements of each group, and
    returns a mapping of categories to their sliced aggregates.
    """
    # Hint: slice lazily using islice inside the grouping loop!
    pass

if __name__ == "__main__":
    records = [
        {"category": "A", "val": 10},
        {"category": "A", "val": 20},
        {"category": "A", "val": 30},
        {"category": "A", "val": 40},
        {"category": "B", "val": 5},
        {"category": "B", "val": 15},
        {"category": "B", "val": 25},
        {"category": "B", "val": 35},
    ]
    print(f"Baseline: {process_data_pipeline_baseline(records)}")
    itertools_out = process_data_pipeline_itertools(records)
    print(f"Itertools: {itertools_out}")
