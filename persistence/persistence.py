import json
from pathlib import Path

from serialisation import event_to_json

from ..main import *

path = Path("events.json")

evenzi: str = event_to_json(build_event(1))


def json_to_file(data: str, path) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(evenzi, file)
        return


def save_event() -> None:
    pass


print(json_to_file(evenzi, path))
