"""
Exercise 5: Chunked Processing of Large Files
Task: Process a large CSV line by line to sum categories.
"""
import csv
import os

# TODO: Implement an incremental CSV reader generator
def stream_csv_records(file_path):
    """Yields rows incrementally from the CSV file as dict records."""
    pass

if __name__ == "__main__":
    csv_file = "raw_data.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "amount"])
        writer.writerow(["hardware", "150.00"])
        writer.writerow(["software", "49.99"])
        writer.writerow(["hardware", "350.00"])
        writer.writerow(["software", "150.00"])
    totals = {}
    records_stream = stream_csv_records(csv_file)
    if records_stream is not None:
        for row in records_stream:
            cat = row["category"]
            amt = float(row["amount"])
            totals[cat] = totals.get(cat, 0.0) + amt
        print(f"Final aggregated totals: {totals}")
    os.remove(csv_file)
