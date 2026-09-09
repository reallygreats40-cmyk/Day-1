"""
Advanced Data Handling & Manipulation
Topic: Stream File I/O -- Chunked Processing of Bulk Text Files

"""

import csv


def generate_csv_rows(path):
    """Yields rows incrementally from a CSV file."""
    with open(path, newline="") as f:
        yield from csv.DictReader(f)  # delegate to DictReader's own iterator


def main():
    # Write a dummy sales CSV
    with open("sales.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "amount"])
        writer.writerow(["electronics", "299.99"])
        writer.writerow(["books", "15.50"])
        writer.writerow(["electronics", "45.00"])
        writer.writerow(["books", "120.00"])

    totals = {}
    for row in generate_csv_rows("sales.csv"):
        category = row["category"]
        amount = float(row["amount"])
        totals[category] = totals.get(category, 0.0) + amount  # running total

    print(f"Final aggregated totals: {totals}")


if __name__ == "__main__":
    main()
