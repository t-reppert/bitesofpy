import json
from pathlib import Path
from datetime import datetime
from pprint import pprint as pp
SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path('/tmp')


def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    belts = list(zip(SCORES, BELTS))
    belt_dict = {}
    with open(data) as d:
        j = json.load(d)
    score = 0
    for s in sorted(j, key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y")):
        day = datetime.strptime(s['date'], "%m/%d/%Y").strftime("%B %d, %Y")
        score += s["score"]
        for i in range(len(BELTS)-1,-1,-1):
            if score >= belts[i][0]:
                if belts[i][1] not in belt_dict:
                    belt_dict[belts[i][1]] = day
        
    return belt_dict
