import json
import main
from pathlib import Path


path = Path("events.json")

evenzi = main.build_event(1)

def json_to_file(data: str, path) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(evenzi, file)
        return

def save_event() -> None:
    
