#!/usr/bin/env python

# from dataclasses import dataclass
from datetime import datetime

from models import Calendar, Event, Person


def get_title() -> str:
    prompt: str = "Title: "
    title: str = input(prompt)
    return title


# what_author currently returns the building blocks of the author but does not create the object itself
def get_author() -> tuple[str, str]:
    name_prompt = "Enter your name: "
    email_prompt = "Enter your email: "
    author_name = input(name_prompt)
    author_email = input(email_prompt)

    return author_name, author_email


def get_events(events: list[Event], calendar_id: int) -> list[Event]:
    return [event for event in events if event.calendar_id == calendar_id]


# Instantiates the classes and runs all code within (runs as script)
if __name__ == "__main__":
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

    print("Type of events object**************************************")
    print("****************************************")
    print("****************************************")
    # print("Type of get_events object**************************************")
    # print(type(get_events))
    # print("****************************************")
    # print("****************************************")
    # print("Events in calendar 1**************************************")
    # print("****************************************")
    # print("****************************************")
    print(get_events(events, 1))
    print("****************************************")
    print("****************************************")
    # print("Events in calendar 2**************************************")
    # print("****************************************")
    # print("****************************************")
    print(get_events(events, 2))
    # print("Events in calendar 3**************************************")
    print("****************************************")
    print("****************************************")
    print(type(get_author()))
    print("****************************************")
    print("****************************************")
    # print("EOL**************************************")
    # print("***************************************")
    # print("***************************************")
