import json
from dateutil.tz import gettz
from datetime import date, timedelta, tzinfo, datetime
from pathlib import Path
from typing import Tuple, Optional, List
from dateutil.parser import parse
from collections import defaultdict
from pprint import pprint
import os

DATA_FILE_NAME = "test1.json"
TMP = Path(os.getenv("TMP", "/tmp"))
DATA_PATH = TMP / DATA_FILE_NAME
MY_TZ = gettz("America/New York")
UTC = gettz("UTC")


def longest_streak(
    data_file: Path = DATA_PATH, my_tz: Optional[tzinfo] = MY_TZ
) -> Optional[Tuple[date, date]]:
    """Retrieve datetime strings of passed commits and calculate the longest
    streak from the user's data

    Note: The datetime strings will need to be used to create aware datetime objects

    All datetimes are in UTC, and the timezone of the user is part of the context
    for calculating a streak. Ex: 2019-10-14 01:58:48.129585+00:00 is 2019-10-13 in
    New York City. You will need to convert datetimes from UTC into the supplied timezone.

    The tests show an example of how a streak can change based on the timezone used.

    If the dataset has two or more streaks of the same length as longest, provide
    only the most recent streak.

    Return a tuple containing start and end date for the longest streak
    or None
    """
    longest_streak = tuple()
    with open(data_file) as f:
        data = json.load(f)
    commits = {parse(d['date']).astimezone(my_tz).toordinal() for d in data['commits'] if d['passed'] == True}
    commits = sorted(commits)

    if not commits:
        return None

    start_date = commits[0]
    end_date = commits[0]
    streak = 1
    temp_streak = 1
    longest_streak = (start_date, end_date)
    for i in range(len(commits)-1):
        if commits[i+1] - commits[i] > 1:
            end_date = commits[i]
            current_longest = longest_streak[1] - longest_streak[0]
            diff = end_date - start_date
            if diff > current_longest:
                longest_streak = (start_date, end_date)
            start_date = commits[i+1]
            if temp_streak > streak:
                streak = temp_streak
            temp_streak = 1
        elif commits[i+1] - commits[i] == 1 and i+1 == len(commits) - 1:
            temp_streak += 1
            end_date = commits[i+1]
            if temp_streak >= streak:
                longest_streak = (start_date, end_date)
        else:
            temp_streak += 1
            end_date = commits[i+1]

    return (date.fromordinal(longest_streak[0]), date.fromordinal(longest_streak[1]))



if __name__ == "__main__":
    streak = longest_streak(data_file='/tmp/test2.json')
    #print(f"My longest streak went from {streak[0]} through {streak[1]}")
    #print(f"The streak lasted {(streak[1]-streak[0]).days + 1} days")
