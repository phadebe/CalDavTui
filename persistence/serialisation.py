from datetime import datetime
from uuid import UUID


def serialise_default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    elif isinstance(o, UUID):
        return str(o)

    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
