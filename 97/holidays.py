from collections import defaultdict
import os
import re
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = Soup(content, 'html.parser')
    for tr in soup.select('table.list-table tr'):
        cells = tr.findAll('td')
        if len(cells) > 0:
            date = cells[1].text.strip()
            month = re.search(r'-(\d+)-',date).group(1)
            holiday = cells[3].text.lstrip()[:-1]
            holidays[month].append(holiday)
    return holidays

