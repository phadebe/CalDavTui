from datetime import datetime, timedelta

from models import Calendar, Event, Person

# Default timezone for testing
TZ = ZoneInfo("Africa/Johannesburg")

# Predefined actors & calendars
default_creator = Person(name="Simon Peach", email="simonpeach@gmail.com")
work_creator = Person(name="John Doe", email="johndoe@work.com")

calendars = [
    Calendar(id=1, name="Personal", colour="Green"),
    Calendar(id=2, name="Work", colour="Blue"),
    Calendar(id=3, name="School", colour="Red"),
]


def make_test_event(
    title: str = "Sample Meeting",
    start: datetime | None = None,
    duration_hours: float = 1.0,
    calendar_id: int = 1,
    creator: Person = default_creator,
    description: str | None = None,
) -> Event:

    if start is None:
        # Defaults to today at 09:00 SAST if no start time is specified
        now = datetime.now(tz=TZ)
        start = now.replace(
            hour=9,
            minute=0,
            second=0,
            microsecond=0,
        )

    end = start + timedelta(hours=duration_hours)

    return Event(
        title=title,
        start=start,
        end=end,
        creator=creator,
        calendar_id=calendar_id,
        description=description,
    )


base_date = datetime(2026, 10, 7, tzinfo=TZ)

sample_events = [
    # 1. Standup: 09:00 - 09:30 on Work calendar
    make_test_event(
        title="Morning Standup",
        start=base_date.replace(hour=9, minute=0),
        duration_hours=0.5,
        calendar_id=2,
        creator=work_creator,
    ),
    # 2. Lunch: 12:00 - 13:00 on Personal calendar
    make_test_event(
        title="Lunch with Alex",
        start=base_date.replace(hour=12, minute=0),
        duration_hours=1.0,
        calendar_id=1,
    ),
    # 3. Afternoon Lecture: 14:00 - 16:00 on School calendar
    make_test_event(
        title="IFS242 Lecture",
        start=base_date.replace(hour=14, minute=0),
        duration_hours=2.0,
        calendar_id=3,
        description="Database normalization and ER diagrams",
    ),
    # 4. Defaults test: uses default time (09:00 today),
    # default person, 1 hour
    make_test_event(title="Quick Reminder"),
]
