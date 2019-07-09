# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    parse_regex = re.compile(r'(?P<social>\w+)[\n\s]*Min: (?P<min>\d+)[\n\s]*Max: (?P<max>\d+)[\n\s]*Can contain: (?P<regex>.*)\n*')
    social_plat = {}
    for item in parse_regex.finditer(social_platforms):
        social = item.group('social')
        minimum = int(item.group('min'))
        maximum = int(item.group('max'))
        pattern = item.group('regex').replace(' ','')
        rx = r'^['+pattern+']+$'
        regex = re.compile(rx)
        social_plat[social] = Validator(range=range(minimum,maximum),regex=regex)
    return social_plat


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators.keys():
        raise ValueError
    
    matcher = all_validators[platform].regex
    return matcher.match(username) and len(username) in all_validators[platform].range


