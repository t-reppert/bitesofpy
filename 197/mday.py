from datetime import date, timedelta

def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    start = date(year,5,1)
    end = date(year,5,31)
    return [start + timedelta(days=x) for x in range((end-start).days + 1) if (start + timedelta(days=x)).weekday() == 6][1]

