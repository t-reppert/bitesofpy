from datetime import datetime

BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')
py2_ends = datetime(2020,4,12)

def py2_earth_hours_left():
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth"""
    difference = BITE_CREATED_DT - py2_ends
    return round(abs(difference.total_seconds()/60/60),2)


def py2_miller_min_left():
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller"""
    earth_hours_per_miller_hour = 365*24*7
    py2_earth_hours = py2_earth_hours_left()
    return round((py2_earth_hours/earth_hours_per_miller_hour)*60,2)