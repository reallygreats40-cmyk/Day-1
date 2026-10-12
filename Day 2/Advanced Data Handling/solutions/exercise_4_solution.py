import json
from dataclasses import dataclass, asdict, is_dataclass

@dataclass
class OrderRecord:
    order_id: str
    price: float
    quantity: int

class OrderEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            # convert to a plain, serialisable dict
            return asdict(obj)
        # preserve normal error behaviour for other types
        return super().default(obj)

order = OrderRecord("ORD_101", 45.50, 10)
payload = json.dumps(order, cls=OrderEncoder)
print(f"Encoded JSON: {payload}")

decoded_dict = json.loads(payload)
restored = OrderRecord(**decoded_dict)  # rebuild the dataclass
print(f"Restored Record Object: {restored}")
