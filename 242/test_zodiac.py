from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)

def test_get_sign_with_most_people(signs):
    actual = get_sign_with_most_famous_people(signs)
    assert actual == ('Scorpio', 35)
    assert actual != ('Gemini', 15)

@pytest.mark.parametrize('sign1,sign2,expected',[
    ('Gemini','Libra', True),
    ('Taurus','Capricorn', True),
    ('Gemini','Pisces', False),
    ('Aries','Scorpio', False),
    ('Aries','Blah', False),
    ('Blah','Blearg', False),
    (1,2, False),
])
def test_signs_are_mutually_compatible(signs, sign1, sign2, expected):
    assert signs_are_mutually_compatible(signs,sign1,sign2) == expected


def test_get_sign_by_date(signs):
    date = datetime(year=2021, month=6, day=13)
    actual = get_sign_by_date(signs, date)
    assert actual == 'Gemini'
    date = datetime(year=2021, month=1, day=15)
    actual = get_sign_by_date(signs, date)
    assert actual == 'Capricorn'
    date = datetime(year=2021, month=3, day=20)
    actual = get_sign_by_date(signs, date)
    assert actual == 'Pisces'
    date = datetime(year=2021, month=2, day=19)
    actual = get_sign_by_date(signs, date)
    assert actual == 'Pisces'
