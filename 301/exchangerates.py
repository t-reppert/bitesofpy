import os
from datetime import date, timedelta, datetime
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
import json


URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    dates = [start_date + timedelta(days=x) for x in range(0, (end_date-start_date).days+1)]
    return dates


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    sorted_daily_rates = [k for k in sorted(daily_rates.keys())]
    earliest_date = sorted_daily_rates[0].split('-')
    latest_date = sorted_daily_rates[-1].split('-')
    if start < date(year=int(earliest_date[0]), month=int(earliest_date[1]), day=int(earliest_date[2])) \
        or end > date(year=int(latest_date[0]), month=int(latest_date[1]), day=int(latest_date[2])):
        raise ValueError
    days = get_all_days(start, end)
    date_dict = {}
    open_date = start - timedelta(days=1)
    for day in days:
        if day.strftime("%Y-%m-%d") in daily_rates:
            date_dict[day] = day
            open_date = day
        else:
            date_dict[day] = open_date
    return date_dict


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    daily_rates = json.loads(RATES_FILE.read_text())["rates"]
    date_dict = match_daily_rates(start, end, daily_rates)
    exchange_rate_dict = {}
    for date, base_date in date_dict.items():
        base_date_str = base_date.strftime("%Y-%m-%d")
        exchange_rate_dict[date] = {"Base Date": base_date, "USD": daily_rates[base_date_str]["USD"], "GBP": daily_rates[base_date_str]["GBP"]}
    return exchange_rate_dict

