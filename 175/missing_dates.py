from datetime import date, timedelta

def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    dates = sorted(dates)
    set_of_dates = set(dates[0] + timedelta(x) for x in range((dates[-1] - dates[0]).days))
    return sorted(set_of_dates - set(dates))
    