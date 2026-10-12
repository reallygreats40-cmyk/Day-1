from dataclasses import dataclass, field

@dataclass
class Customer:
    name: str
    age: int
    tags: list[str] = field(default_factory=list)  # new list per customer

    def __post_init__(self):
        """Runs straight after __init__: clean, then validate."""
        self.name = self.name.strip()
        if not self.name:
            raise ValueError("Customer name cannot be empty.")
        if self.age < 0:
            raise ValueError("Age must be zero or positive.")

def main():
    valid = Customer("  Ada Lovelace ", 36, ["pioneer"])
    print(f"Valid: {valid}")

    try:
        Customer("Bob", -5)               # invalid age
    except ValueError as err:
        print(f"Rejected: {err}")

if __name__ == "__main__":
    main()
