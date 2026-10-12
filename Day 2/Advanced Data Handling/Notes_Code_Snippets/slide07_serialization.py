import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Event:
    name: str
    timestamp: datetime          # json cannot encode this type by itself

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()      # datetime to ISO text
        return super().default(obj)     # anything else: normal error

def main():
    event = Event("system_boot", datetime(2026, 1, 1, 9, 30))

    # Serialise: object -> dict -> JSON text
    payload = json.dumps(asdict(event), cls=CustomEncoder)
    print(f"JSON: {payload}")

    # Deserialise: JSON text -> dict -> object
    data = json.loads(payload)
    data["timestamp"] = datetime.fromisoformat(data["timestamp"])
    restored = Event(**data)
    print(f"Restored equal: {restored == event}")   # True

if __name__ == "__main__":
    main()
