from itertools import islice, groupby

def process_data_pipeline_itertools(raw_records):
    # groupby only groups *consecutive* items, so sort by key first
    sorted_records = sorted(
        raw_records, key=lambda x: x["category"])
    grouped_totals = {}
    for key, group in groupby(
            sorted_records, key=lambda x: x["category"]):
        # islice pulls the first 3 items directly from the group
        # iterator -- no intermediate list is ever built
        first_three = islice(group, 3)
        grouped_totals[key] = sum(
            item["val"] for item in first_three)
    return grouped_totals

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
print(process_data_pipeline_itertools(records))
