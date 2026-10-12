"""
Exercise 3: Structured Data with Dataclasses and Validation
Task: Create a validated OrderRecord dataclass.
"""
from dataclasses import dataclass

# TODO: Implement ordered record fields with post-init validation
@dataclass
class OrderRecord:
    order_id: str
    price: float
    quantity: int
    customer_id: str

    def __post_init__(self):
        """
        Validate fields:
        - Price must be greater than zero.
        - Quantity must be greater than zero.
        - customer_id must not be empty.
        """
        # Add your parameter validation guards here
        pass

if __name__ == "__main__":
    try:
        # 1. Valid Record
        valid = OrderRecord("ORD_001", 15.99, 3, "CUST_99")
        print(f"Order created successfully: {valid}")
        # 2. Invalid Record (should raise ValueError)
        invalid = OrderRecord("ORD_002", -5.00, 2, "CUST_99")
    except ValueError as e:
        print(f"Validation caught error: {e}")
