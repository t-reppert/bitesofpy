import csv
from csv import DictReader
from pathlib import Path
from urllib.request import urlretrieve
import re

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites = []
    bite_regex = re.compile(r'^Bite (\d+)\.')
    with open(stats, 'r', encoding='utf-8-sig') as f:
        reader = DictReader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        print(reader.fieldnames)
        for row in reader:
            if 'None' not in row['Difficulty']:
                bites.append((row['Bite'],row['Difficulty']))
    bites_sorted = sorted(bites, key=lambda x:x[1], reverse=True)
    bites_selected = []
    for x in bites_sorted[:N]:
        match = bite_regex.search(x[0])
        if match:
            bites_selected.append(match.group(1))
    return bites_selected


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)