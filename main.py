#!/usr/bin/env python

from datetime import datetime
from dataclasses import asdict
from zoneinfo import ZoneInfo
import json

from models import Event, Person


def get_title() -> str:
    prompt: str = "Title: "
    title: str = input(prompt)
    return title


def get_description() -> str:
    prompt: str = "Enter description: "
    description: str = input(prompt)
    return description


def get_author() -> tuple[str, str]:
    name_prompt: str = "Enter your name: "
    email_prompt: str = "Enter your email: "
    author_name: str = input(name_prompt)
    author_email: str = input(email_prompt)

    return author_name, author_email


def get_start_date() -> datetime:
    while True:
        try:
            print("***Please enter start date***")
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            day = int(input("Enter day (1-31): "))
            user_date = datetime(
                year, month, day, tzinfo=ZoneInfo("Africa/Johannesburg")
            )

            return user_date
        except ValueError:
            print("Sorry, please insert valid start date")


def get_end_date() -> datetime:
    while True:
        try:
            print("***Please enter end date***")
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            day = int(input("Enter day (1-31): "))
            user_date = datetime(
                year, month, day, tzinfo=ZoneInfo("Africa/Johannesburg")
            )

            return user_date
        except ValueError:
            print("***Sorry, please insert valid end date***")


def get_events(events: list[Event], calendar_id: int) -> list[Event]:
    return [event for event in events if event.calendar_id == calendar_id]


def build_event(calendar_id: int) -> Event:
    title = get_title()
    author_name, author_email = get_author()
    creator = Person(name=author_name, email=author_email)
    start_date = get_start_date()
    end_date = get_end_date()
    description = get_description()
    return Event(
        title=title,
        start=start_date,
        end=end_date,
        creator=creator,
        calendar_id=calendar_id,
        description=description,
    )


def event_to_dict(Event):
    return json.dumps(asdict()))


if __name__ == "__main__":

    print("****************************************")
    print("****************************************")
    print(f"{event_to_dict(build_event(1))}")
    print("****************************************")
    print("****************************************")
