from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> datetime:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    hours_regex = re.compile(r'(?P<hours>\d+)h')
    minutes_regex = re.compile(r'(?P<minutes>\d+)m')
    seconds_regex = re.compile(r'(?P<seconds>\d+)s')
    seconds_alone = re.compile(r'^(\d+)$')
    days_regex = re.compile(r'(?P<days>\d+)d')
    hours = 0
    minutes = 0
    seconds = 0
    days = 0
    if hours_regex.search(delay_time):
        hours = int(hours_regex.search(delay_time).group("hours"))
    if minutes_regex.search(delay_time):
        minutes = int(minutes_regex.search(delay_time).group("minutes"))
    if seconds_regex.search(delay_time):
        seconds = int(seconds_regex.search(delay_time).group("seconds"))
    if days_regex.search(delay_time):
        days = int(days_regex.search(delay_time).group("days"))
    if seconds_alone.search(delay_time):
        seconds = int(seconds_alone.search(delay_time).group(1))
    target_time = start_time + timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
    return f"{task} @ {target_time:%Y-%m-%d %H:%M:%S}"
    