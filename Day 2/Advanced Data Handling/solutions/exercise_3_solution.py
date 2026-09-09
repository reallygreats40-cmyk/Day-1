from dataclasses import dataclass

@dataclass
class OrderRecord:
    order_id: str
    price: float
    quantity: int
    customer_id: str

    def __post_init__(self):
        # runs automatically right after the generated __init__
        if self.price <= 0:
            raise ValueError("price must be positive.")
        if self.quantity <= 0:
            raise ValueError("quantity must be positive.")
        if not self.customer_id:
            raise ValueError("customer_id must not be empty.")

valid = OrderRecord("ORD_001", 15.99, 3, "CUST_99")
print(f"Order created successfully: {valid}")

try:
    invalid = OrderRecord("ORD_002", -5.00, 2, "CUST_99")
except ValueError as e:
    print(f"Validation caught error: {e}")
