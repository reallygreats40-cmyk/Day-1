"""
Exercise 4: Safe Serialization with Custom JSON Encoders
Task: Build a custom JSONEncoder for OrderRecord instances.
"""
import json
from dataclasses import dataclass, asdict

@dataclass
class OrderRecord:
    order_id: str
    price: float
    quantity: int

# TODO: Implement a custom JSON Encoder class
class OrderEncoder(json.JSONEncoder):
    def default(self, obj):
        # Hint: if obj is a dataclass instance, use asdict()
        pass

if __name__ == "__main__":
    order = OrderRecord("ORD_101", 45.50, 10)
    try:
        # json.dumps fails on custom classes without an encoder
        payload = json.dumps(order, cls=OrderEncoder)
        print(f"Encoded JSON: {payload}")
        decoded_dict = json.loads(payload)
        print(f"Decoded dictionary: {decoded_dict}")
    except TypeError as e:
        print(f"Type error during serialization: {e}")
