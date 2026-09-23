import json
from dataclasses import asdict
from datetime import datetime
from uuid import UUID


from ..models import *

# Serialisation of Objects to JSON


def serialise_default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    elif isinstance(o, UUID):
        return str(o)

    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")


def event_to_json(event: Event) -> str:
    return json.dumps(
        asdict(event),
        default=serialise_default,
    )


# Deserialisation of Objects to JSON


def json_to_event():
    with open("events.json") as file:
        d = json.load(file)
        print(d)
