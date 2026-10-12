import csv

def generate_csv_rows(path):
    """Yields one row (as a dict) at a time from a CSV file."""
    with open(path, newline="") as f:
        yield from csv.DictReader(f)

def main():
    # Create a small sample CSV
    with open("sales.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "amount"])
        writer.writerows([["electronics", "299.99"], ["books", "15.50"],
                          ["electronics", "45.00"], ["books", "120.00"]])

    # Aggregate as rows arrive: memory depends on categories, not rows
    totals = {}
    for row in generate_csv_rows("sales.csv"):
        category = row["category"]
        totals[category] = totals.get(category, 0) + float(row["amount"])

    for category, total in totals.items():
        print(f"{category}: {total:.2f}")

if __name__ == "__main__":
    main()
