import csv
import os
import tracemalloc
import pandas as pd
from dataclasses import dataclass

@dataclass
class Transaction:
    id_code: str
    category: str
    amount: float

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative.")

def lazy_csv_stream(file_path):
    with open(file_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            yield row  # Stage 1: raw rows, one at a time

def validate_and_filter_stream(records_iterator):
    for row in records_iterator:
        try:
            yield Transaction(row["id_code"], row["category"],
                               float(row["amount"]))
        except ValueError:
            continue  # Stage 2: invalid rows skipped quietly


def aggregate_and_load_pandas(validated_iterator):
    categories, amounts = [], []
    # Stage 3: consume the validated stream
    for txn in validated_iterator:
        categories.append(txn.category)
        amounts.append(txn.amount)
    cat_series = pd.Series(categories, dtype="category")
    amt_series = pd.Series(amounts, dtype="float32")
    return pd.DataFrame({
        "category": cat_series,
        "amount": amt_series,
    })


if __name__ == "__main__":
    # Setup: create the sample CSV this pipeline reads (matches the exercise)
    csv_file = "pipeline_data.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id_code", "category", "amount"])
        for i in range(5000):
            cat = "hardware" if i % 2 == 0 else "software"
            writer.writerow([f"TX_{i}", cat, f"{10.5 * (i % 5)}"])
            # Inject a few invalid negative rows
            if i % 500 == 0:
                bad_row = [f"TX_ERR_{i}", "hardware", "-100.00"]
                writer.writerow(bad_row)

    tracemalloc.start()
    try:
        raw_stream = lazy_csv_stream(csv_file)
        valid_stream = validate_and_filter_stream(raw_stream)
        df_result = aggregate_and_load_pandas(valid_stream)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Shape: {df_result.shape}")
        print(f"Peak memory: {peak / 1024:.2f} KB")
    finally:
        tracemalloc.stop()
        if os.path.exists(csv_file):
            os.remove(csv_file)
