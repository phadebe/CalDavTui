#!/usr/bin/env python

import json
from dataclasses import asdict
from datetime import datetime

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


def get_date(start_or_end: str) -> datetime:
    while True:
        try:
            print(f"***Please enter {start_or_end} date***")
            user_input = input("Enter date and time (DD-MM-YYYY HH:MM): ")
            date_input = f"{user_input} +0200"
            format_layout = "%d-%m-%Y %H:%M %z"
            date_of = datetime.strptime(date_input, format_layout)
            return date_of
        except ValueError:
            print(f"Sorry, {start_or_end} date was invalid")


def get_events(events: list[Event], calendar_id: int) -> list[Event]:
    return [event for event in events if event.calendar_id == calendar_id]


def build_event(calendar_id: int) -> Event:
    title = get_title()
    author_name, author_email = get_author()
    creator = Person(name=author_name, email=author_email)
    start_date = get_date("start")
    end_date = get_date("end")
    description = get_description()
    return Event(
        title=title,
        start=start_date,
        end=end_date,
        creator=creator,
        calendar_id=calendar_id,
        description=description,
    )


def event_to_json(event: Event) -> str:
    return json.dumps(asdict(event), default=str)


if __name__ == "__main__":

    print("****************************************")
    print("****************************************")
    event1 = build_event(1)
    print(event_to_json(event1))
    print("****************************************")
    print("****************************************")
