"""
Advanced Data Handling & Manipulation
Topic: Serialization -- Portability and Safe Custom JSON Encoding

"""

import json
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Event:
    name: str
    timestamp: datetime  # json.dumps can't handle this type alone


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # convert to a JSON-safe string
        return super().default(obj)  # keep normal behaviour otherwise


def main():
    event = Event("system_boot", datetime.now())

    # Serialize to JSON using the custom encoder
    payload = json.dumps(asdict(event), cls=CustomEncoder)
    print(f"JSON Payload: {payload}")

    # Restore: parse the JSON back to a dict, then rebuild the dataclass.
    # datetime needs to be parsed back explicitly -- json.loads has no
    # way to know that string was originally a datetime.
    restored_dict = json.loads(payload)
    restored_dict["timestamp"] = datetime.fromisoformat(restored_dict["timestamp"])
    restored_event = Event(**restored_dict)
    print(f"Restored Event: {restored_event}")


if __name__ == "__main__":
    main()
