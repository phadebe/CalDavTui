from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Person:
    name: str
    email: str


@dataclass
class Event:  # parameter order = required, optional, logic dependant
    title: str
    start: datetime
    end: datetime
    creator: Person
    calendar_id: int
    description: str | None = None

    id: UUID = field(default_factory=uuid4)


@dataclass
class Calendar:
    id: int
    name: str
    colour: str
