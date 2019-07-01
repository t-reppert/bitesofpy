from datetime import date
from dateutil.parser import parse
from dateutil.rrule import rrule, DAILY

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    return [ d.date() for d in list(rrule(DAILY, byweekday=[0,1,2,3,4],count=100,dtstart=start_date)) ]