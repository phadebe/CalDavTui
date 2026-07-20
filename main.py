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
    calendar_id = 1
    prompt = "(W)ork or (P)ersonal account? \n"
    calendar_name: str = input(prompt).strip().upper()
    if calendar_name == "W":
        calendar_id = 1
    elif calendar_name == "P":
        calendar_id = 2
    return calendar_id


# def get_title(title: str) -> str:
#
