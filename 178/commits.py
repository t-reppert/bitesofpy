from collections import Counter, defaultdict
import os
from urllib.request import urlretrieve
import re
from dateutil.parser import parse

commits = os.path.join('/tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'

def line_parser(line):
    line_regex = re.compile(r"^Date:\s+(?P<date>.*) \| \d+ file")
    insert_regex = re.compile(r" (?P<insertions>\d+) insertion")
    delete_regex = re.compile(r" (?P<deletions>\d+) deletion")
    match = line_regex.search(line)
    inserts = insert_regex.search(line)
    deletes = delete_regex.search(line)
    changes = 0
    if match:
        if inserts:
            changes += int(inserts.group('insertions'))
        if deletes:
            changes += int(deletes.group('deletions'))
        return (parse(match.group('date')), changes)

def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    commits = defaultdict(int)
    with open(commit_log) as f:
        data = f.readlines()
    if year:
        # parse only this year in file
        for line in data:
            date, changes = line_parser(line)
            if date.year == year:
                commits[date.strftime("%Y-%m")] += changes

    else:
        # parse whole file
        for line in data:
            d, changes = line_parser(line)
            commits[d.strftime("%Y-%m")] += changes
    
    sorted_commits = sorted(commits.items(),key=lambda kv:kv[1],reverse=True)
    return (sorted_commits[-1][0],sorted_commits[0][0])

