import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc_dt = pytz.utc.localize(utc)
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError
        tzone = pytz.timezone(tz)
        if int(utc_dt.astimezone(tzone).hour) not in list(MEETING_HOURS):
            return False
    return True