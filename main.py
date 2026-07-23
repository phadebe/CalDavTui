#!/usr/bin/env python

from dataclasses import dataclass
from datetime import datetime

# from email.utils import formataddr

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


@dataclass
class Person:
    name: str
    email: str


@dataclass
class Event:
    id: int
    title: str
    start: datetime
    end: datetime
    description: str | None
    creator: Person

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
    #
    # print(what_author(default_name="John Doe", default_email="johndoe@gmail.com"))


# Instantiates the classes and runs all code within (runs as script)
if __name__ == "__main__":
    creator1 = Person(name="Philasande Hadebe", email="philasand2010@gmail.com")

    event1 = Event(
        id=1,
        title="My Birthday",
        start=datetime(2005, 8, 22),
        end=datetime(2005, 8, 22),
        description=None,
        creator=creator1,
    )
    print("***")
    print(creator1)
    print("***")
    print(event1)
