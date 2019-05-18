import os
import urllib.request
import re

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    prev_book = ''
    book = ''
    chart = {}
    with open(LOG,'r') as f:
        for line in f:
            fields = re.split(r'\s+',line.strip(),maxsplit=4)
            if 'sending to slack channel' not in fields[4]:
                prev_book = fields[4]
                continue
            else:
                if 'python' in prev_book.lower():
                    book = PY_BOOK
                else:
                    book = OTHER_BOOK
                if fields[0] not in chart:
                    chart[fields[0]] = book
                else:
                    chart[fields[0]] += book
    for k,v in chart.items():
        print(f'{k} {v}')

