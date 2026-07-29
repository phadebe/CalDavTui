from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar


@dataclass
class Person:
    name: str
    email: str


@dataclass
class Event:
    id: int = field(init=False)

    _next_id: ClassVar[int] = 0

    def __post_init__(self):
        self.id = Event._next_id
        Event._next_id += 1

    title: str
    start: datetime
    end: datetime
    description: str | None
    creator: Person
