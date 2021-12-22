import os
from pathlib import Path
from urllib.request import urlretrieve
import requests
from collections import defaultdict
import re

from dateutil.parser import parse

# get the data
TMP = Path(os.getenv("TMP", "/tmp"))
base_url = 'https://bites-data.s3.us-east-2.amazonaws.com/'

fathers_days_countries = TMP / 'fathers-day-countries.txt'
fathers_days_recurring = TMP / 'fathers-day-recurring.txt'

for file_ in (fathers_days_countries, fathers_days_recurring):
    if not file_.exists():
        urlretrieve(base_url + file_.name, file_)


def _parse_father_days_per_country(year, filename=fathers_days_countries):
    """Helper to parse fathers_days_countries"""
    if year == None:
        year = str(2020)
    with open(fathers_days_countries) as f:
        lines = [l.rstrip() for l in f]
    dates_dict = defaultdict(list)
    date_regex2 = re.compile(r'^'+str(year)+': ([a-zA-Z 0-9]+)')
    for line in lines:
        matched = date_regex2.search(line)
        if line.startswith('#'):
            continue
        if line.startswith('*'):
            line = line.lstrip('* ')
            line = line.replace(' and ', ' ')
            countries = [c.strip() for c in line.split(',')]
        elif matched:
            d = matched.group(1)
            dates_dict[d].extend(countries)
        else:
            continue
    return dates_dict

def _parse_recurring_father_days(filename=fathers_days_recurring):
    """Helper to parse fathers_days_recurring"""
    with open(fathers_days_recurring) as f:
        lines = [l.rstrip() for l in f]
    date_regex = re.compile(r'^\* ([a-zA-Z 0-9]+)')
    dates_dict = defaultdict(list)
    date = None
    for line in lines:
        if line.startswith('#'):
            continue
        if line.startswith('*'):
            matched = date_regex.search(line)
            date = matched.group(1)
        elif line:
            dates_dict[date].append(line)
    return dates_dict

def get_father_days(year=2020):
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    dict1 = _parse_father_days_per_country(year)
    dict2 = _parse_recurring_father_days()
    dict2.update(dict1)
    return dict2


def generate_father_day_planning(father_days=None):
    """Prints all father days in order, example in tests and
       Bite description
    """
    if father_days is None:
        father_days = get_father_days()

    for k in sorted(father_days.keys(), key=parse):
        print(k)
        for country in father_days[k]:
            print(f"- {country}")
        print()