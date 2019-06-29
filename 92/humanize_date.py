from collections import namedtuple
from datetime import datetime,timedelta


TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if type(date) != datetime:
        raise ValueError
    if date > NOW:
        raise ValueError
    offset = int((NOW - date).total_seconds())
    offset_date = NOW - timedelta(seconds=offset)
    print(offset)
    print(offset_date.strftime('%m/%d/%y'))
    for i in range(0,len(TIME_OFFSETS)-1):
        if offset >= 2*DAY:
            return offset_date.strftime('%m/%d/%y')
        if offset < 10:
            return TIME_OFFSETS[0].date_str
        if offset == 10:
            return TIME_OFFSETS[1].date_str.format(offset)
        if offset >= TIME_OFFSETS[i].offset and offset < TIME_OFFSETS[i+1].offset:
            if TIME_OFFSETS[i+1].divider:
                value = offset // TIME_OFFSETS[i+1].divider
            else:
                value = offset
            return TIME_OFFSETS[i+1].date_str.format(value)
        
