import csv
import os

def stream_csv_records(file_path):
    # "with" guarantees the file closes on early exit too
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row  # one row at a time, not the whole file

# Setup: create the sample CSV this snippet reads (matches the exercise)
csv_file = "raw_data.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["category", "amount"])
    writer.writerow(["hardware", "150.00"])
    writer.writerow(["software", "49.99"])
    writer.writerow(["hardware", "350.00"])
    writer.writerow(["software", "150.00"])

totals = {}
for row in stream_csv_records(csv_file):
    cat = row["category"]
    amt = float(row["amount"])
    totals[cat] = totals.get(cat, 0.0) + amt  # running total
print(f"Final aggregated totals: {totals}")
os.remove(csv_file)
