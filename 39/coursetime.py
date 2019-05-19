from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    timestamp_regex = re.compile(r'\((\d+:\d+)\)')
    timestamps = []
    with open(COURSE_TIMES,'r') as f:
        for line in f:
            if timestamp_regex.search(line):
                timestamps.append(timestamp_regex.search(line).group(1))
    return timestamps

def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    s = timedelta(seconds=0)
    for timestamp in timestamps:
        minute, second = timestamp.split(':')
        s += timedelta(minutes=int(minute),seconds=int(second))
    return str(s)

