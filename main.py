#!/usr/bin/env python

# from dataclasses import dataclass
from datetime import datetime
from models import Event, Person, Calendar

"""
Add basic functionality
to ask a user to add an
event to their calendar
Event contains:
    0. CalendarId
    1. Title
    2. EventId
    3. Start Date
    4. End Date
    5. Author
    6. Desciption
    7. Colour
"""


# def pick_calendar(default_calendar_id: int) -> int:
#     prompt = (
#         "(W)ork or (P)ersonal account? \n"
#         f"Press Enter to use your Default Calendar ({default_calendar_id}) "
#     )
#     calendar_name: str = input(prompt).strip().upper()
#     if calendar_name == "W":
#         return 1
#     elif calendar_name == "P":
#         return 2
#
#     return default_calendar_id
#
#
# def get_title(title: str) -> str:
#     prompt = "Title: "
#     title = input(prompt)
#     return title
#
#
# # print(pick_calendar(default_calendar_id=5))
# # print(get_title("first title"))
# # 5. Author Allow any string for [Name Surname]
# # but impose structure on email@addre.ss.com
# def what_author(default_name: str, default_email: str):
#     name_prompt = "Enter your name: "
#     email_prompt = "Enter your email: "
#     author_name = input(name_prompt)
#     author_email = input(email_prompt)
#
#     if not author_name:
#         author_name = default_name
#
#     if not author_email:
#         author_email = default_email
#
#     formatted = formataddr((author_name, author_email))
#     return formatted
#
##

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

    def get_events(events: list[Event], calendar_id: int) -> list[Event]:
        matching_events: list[Event] = []
        for event in events:
            if event.calendar_id == calendar_id:
                matching_events.append(event.title)

        return matching_events

    print("*1*Type of events object**************************************")
    print("****************************************")
    print("****************************************")
    print(type(events))
    print("****************************************")
    print("****************************************")
    print("*2*Type of get_events object**************************************")
    print(type(get_events))
    print("****************************************")
    print("****************************************")
    print("*1*Events in calendar 1**************************************")
    print("****************************************")
    print("****************************************")
    print(get_events(events, 1))
    print("*2*Events in calendar 2**************************************")
    print("****************************************")
    print("****************************************")
    print(get_events(events, 2))
    print("*3*Events in calendar 3**************************************")
    print("****************************************")
    print("****************************************")
    print(get_events(events, 3))
    print("*4*EOL**************************************")
    print("***************************************")
    print("***************************************")
