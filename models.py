from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar


@dataclass
class Person:
    name: str
    email: str


@dataclass
class Event:
    title: str
    start: datetime
    end: datetime
    creator: Person
    calendar_id: int
    description: str | None = None

    id: int = field(init=False)

    _next_id: ClassVar[int] = 0

    def __post_init__(self):
        self.id = Event._next_id
        Event._next_id += 1


@dataclass
class Calendar:
    id: int
    name: str
    colour: str
