from collections import namedtuple
from datetime import date,datetime
from dateutil.parser import parse
from time import mktime
import feedparser

FEED = 'http://projects.bobbelderbos.com/pcc/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return datetime.fromtimestamp(mktime(stime)).date()


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    entries = []
    data = feedparser.parse(feed)
    for post in data.entries:
        date = _convert_struct_time_to_dt(post.published_parsed)
        title = post.title
        link = post.link
        tags = []
        for tag in post.tags:
            tags.append(tag.term.lower())
        entries.append(Entry(date=date,title=title,link=link,tags=tags))
    return entries


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    if '&' in search:
        searches = search.split('&')
        for s in searches:
            if s.lower() not in entry.tags:
                return False
        return True
    elif '|' in search:
        searches = search.split('|')
        for s in searches:
            if s.lower() in entry.tags:
                return True
        return False
    else:
        if search.lower() in entry.tags:
            return True
        return False

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date desc
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()
    max_title_len = max([ len(x.title) for x in entries ])
    while True:
        search_term = input("Search for (q for exit): ")
        if search_term == '':
            print("Please provide a search term")
            continue
        elif search_term == 'q':
            print('Bye')
            break
        found = []
        for entry in entries:
            if filter_entries_by_tag(search_term, entry):
                found.append(entry)
        for entry in sorted(found,key=lambda x:x.date):
            print(f'{entry.date:%Y-%m-%d} | {entry.title:<{max_title_len}} | {entry.link}')
        print()
        f = len(found)
        if f == 1:
            word = "entry"
        else:
            word = "entries"
        print(f'{f} {word} matched "{search_term}"')


        



if __name__ == '__main__':
    main()