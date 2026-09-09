"""
Exercise 8: Capstone - Memory-Efficient Data Pipeline
Task: Streaming + validation + compact pandas dtypes + tracemalloc.
"""
import csv, os, tracemalloc
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

# TODO: Implement step-by-step pipeline segments
def lazy_csv_stream(file_path):
    """Step 1: yield rows line-by-line as raw dicts."""
    pass

def validate_and_filter_stream(records_iterator):
    """Step 2: wrap rows in Transaction, skip invalid ones."""
    pass

def aggregate_and_load_pandas(validated_iterator):
    """Step 3: collect into a DataFrame with compact dtypes."""
    pass


if __name__ == "__main__":
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
        shape = df_result.shape if df_result is not None else None
        print(f"Shape: {shape}")
        print(f"Peak memory: {peak / 1024:.2f} KB")
    finally:
        tracemalloc.stop()
        if os.path.exists(csv_file):
            os.remove(csv_file)
