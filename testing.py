from datetime import datetime

from models import Calendar, Event, Person

creators = [
    Person(name="Simon Peach", email="simonpeach@gmail.com"),
    Person(name="John Doe", email="johndoe@gmail.com"),
]

calendars = [
    Calendar(id=1, name="Personal", colour="Green"),
    Calendar(id=2, name="Work", colour="Blue"),
    Calendar(id=3, name="School", colour="Red"),
]

events = [
    Event(
        title="My Birthday",
        start=datetime(2002, 7, 23),
        end=datetime(2002, 7, 23),
        creator=creators[0],
        calendar_id=calendars[0].id,
        description=None,
    ),
    Event(
        title="Michaels Birthday",
        start=datetime(2005, 8, 22),
        end=datetime(2005, 8, 22),
        creator=creators[0],
        calendar_id=calendars[0].id,
        description=None,
    ),
    Event(
        title="IFS242 Exam",
        start=datetime(2002, 7, 23),
        end=datetime(2002, 7, 23),
        creator=creators[1],
        calendar_id=calendars[1].id,
        description=None,
    ),
    Event(
        title="Workplace Harrasment meeting",
        start=datetime(2002, 7, 23),
        end=datetime(2002, 7, 23),
        creator=creators[1],
        calendar_id=calendars[2].id,
        description=None,
    ),
]
