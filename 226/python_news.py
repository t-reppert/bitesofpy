from collections import namedtuple
import re

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    title_spans = soup.find_all('span',{'class':'title'})
    point_comment_spans = soup.find_all('span',{'class':'controls'})
    title_text = [ s.get_text().strip() for s in title_spans ]
    p_c_text =   [ s.get_text().strip() for s in point_comment_spans ]
    titles = []
    points_regex = re.compile(r'(\d+) point')
    comments_regex = re.compile(r'(\d+) comment')
    for i in range(len(title_text)):
        points = int(points_regex.search(p_c_text[i]).group(1))
        comments = int(comments_regex.search(p_c_text[i]).group(1))
        titles.append(Entry(title=title_text[i],points=points,comments=comments))
    return sorted(titles, key=lambda x: x[1]+x[2], reverse=True)[:top]

