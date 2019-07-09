from datetime import datetime, timedelta, date
import re
TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    date_rx = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
    dates = date_rx.findall(data)
    return sorted(list({ datetime.strptime(d,'%Y-%m-%d').date() for d in dates }),reverse=True)


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    if TODAY - dates[0] > timedelta(days=1):
        return 0
    streak = 1
    for i in range(len(dates)-1):
        if dates[i] - dates[i+1] > timedelta(days=1):
            return streak
        else:
            streak += 1
    return streak
        

