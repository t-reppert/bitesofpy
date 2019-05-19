import csv

import requests

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        return decoded_content
        

def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    cr = csv.DictReader(content.splitlines())
    table = {}
    for row in cr:
        if row['tz'] in table:
            table[row['tz']] += "+"
        else:
            table[row['tz']] = "+"
    max_padding = len(max(table.keys(),key=lambda x:len(x)))
    for k,v in sorted(table.items()):
        pad = " " * (max_padding - len(k))
        print(k + pad + " | " + v )

