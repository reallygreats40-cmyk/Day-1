"""
Advanced Data Handling & Manipulation
Topic: Data Schemas -- Structured Data and post_init Validation

"""

from dataclasses import dataclass, field


@dataclass
class Customer:
    name: str
    age: int
    tags: list[str] = field(default_factory=list)  # avoids one shared list

    def __post_init__(self):
        """Validates age and cleans string whitespace
        after instance creation."""
        self.name = self.name.strip()  # normalise, don't just check
        if self.age < 0:
            raise ValueError("Age must be zero or positive.")
        if not self.name:
            raise ValueError("Customer name cannot be empty.")


def main():
    try:
        valid_user = Customer(" Ada Lovelace ", 36, ["pioneer"])
        print(f"Valid: {valid_user}")

        # This will raise a ValueError
        invalid_user = Customer("Grace Hopper", -5)
        print(f"Valid: {invalid_user}")  # never reached
    except ValueError as e:
        print(f"Validation caught error: {e}")


if __name__ == "__main__":
    main()
