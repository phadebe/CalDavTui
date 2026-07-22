#!/usr/bin/env python

# from datetime import datetime

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


def pick_calendar(default_calendar_id: int) -> int:
    prompt = (
        "(W)ork or (P)ersonal account? \n"
        f"Press Enter to use your Default Calendar ({default_calendar_id}) "
    )
    calendar_name: str = input(prompt).strip().upper()
    if calendar_name == "W":
        return 1
    elif calendar_name == "P":
        return 2

    return default_calendar_id


def get_title(title: str) -> str:
    prompt = "Title: "
    title = input(prompt)
    return title


# print(pick_calendar(default_calendar_id=5))
# print(get_title("first title"))
