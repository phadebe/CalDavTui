#!/usr/bin/env python

# from dataclasses import dataclass

from datetime import date

from models import Calendar, Event, Person


def get_title() -> str:
    prompt: str = "Title: "
    title: str = input(prompt)
    return title


def get_author() -> tuple[str, str]:
    name_prompt: str = "Enter your name: "
    email_prompt: str = "Enter your email: "
    author_name: str = input(name_prompt)
    author_email: str = input(email_prompt)

    return author_name, author_email


def get_start_date() -> date:
    try:
        print("**********Please enter the start date**********")
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        user_date = date(year, month, day)
    except ValueError:
        user_date = date(1970, 1, 1)

    return user_date


def get_end_date() -> date:
    try:
        print("**********Please enter the end date**********")
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        user_date = date(year, month, day)
    except ValueError:
        user_date = date(1970, 1, 1)

    return user_date


def get_events(events: list[Event], calendar_id: int) -> list[Event]:
    return [event for event in events if event.calendar_id == calendar_id]


# def build_event(calendar_id: int):
#     title = get_title()
#     author_name, author_email = get_author()
#     creator = Person(name=author_name, email=author_email)
#     start_date=get_start_date()
#     end_date=get_end_date()
#     return Event(
#         title=title,
#         start=,
#         end=,
#         creator=creator,
#         calendar_id=calendar_id,
#         description: str | None = None
#     )


if __name__ == "__main__":
    #    creators = [
    #        Person(name="Simon Peach", email="simonpeach@gmail.com"),
    #        Person(name="John Doe", email="johndoe@gmail.com"),
    #    ]
    #
    #    calendars = [
    #        Calendar(id=1, name="Personal", colour="Green"),
    #        Calendar(id=2, name="Work", colour="Blue"),
    #        Calendar(id=3, name="School", colour="Red"),
    #    ]
    #
    #    events = [
    #        Event(
    #            title="My Birthday",
    #            start=datetime(2002, 7, 23),
    #            end=datetime(2002, 7, 23),
    #            creator=creators[0],
    #            calendar_id=calendars[0].id,
    #            description=None,
    #        ),
    #        Event(
    #            title="Michaels Birthday",
    #            start=datetime(2005, 8, 22),
    #            end=datetime(2005, 8, 22),
    #            creator=creators[0],
    #            calendar_id=calendars[0].id,
    #            description=None,
    #        ),
    #        Event(
    #            title="IFS242 Exam",
    #            start=datetime(2002, 7, 23),
    #            end=datetime(2002, 7, 23),
    #            creator=creators[1],
    #            calendar_id=calendars[1].id,
    #            description=None,
    #        ),
    #        Event(
    #            title="Workplace Harrasment meeting",
    #            start=datetime(2002, 7, 23),
    #            end=datetime(2002, 7, 23),
    #            creator=creators[1],
    #            calendar_id=calendars[2].id,
    #            description=None,
    #        ),
    #    ]

    print("****************************************")
    print("****************************************")
    print(f"{get_start_date()}")
    print("****************************************")
    print("****************************************")
    print(f"{get_end_date()}")
