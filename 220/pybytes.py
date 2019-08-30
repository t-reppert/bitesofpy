from collections import namedtuple, Counter
import re
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'http://projects.bobbelderbos.com/pcc/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


def _get_sec(time_str):
    """Get Seconds from time string."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(url)['entries']

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [ entry.itunes_episode for entry in self.entries if domain in entry.description ]

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        domains = []
        domain_rgx = re.compile(r"(https?://[^/]+)[\"/\']+")
        for entry in self.entries:
            domains_found = domain_rgx.findall(entry.summary)
            domain_set = set(domains_found)
            domain_set = domain_set - IGNORE_DOMAINS
            domains += list(domain_set)
        return Counter(domains).most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        return len([entry for entry in self.entries if SPECIAL_GUEST in entry.description])

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        durations = [ entry.itunes_duration for entry in self.entries ]
        average = sum(map(lambda f: int(f[0]) * 3600 + int(f[1]) * 60 + int(f[2]),
                          map(lambda f: f.split(':'), durations)))/len(durations)
        max_time = max(durations, key=lambda x: _get_sec(x))
        min_time = min(durations, key=lambda x: _get_sec(x))
        return Duration(int(average), max_time, min_time)


