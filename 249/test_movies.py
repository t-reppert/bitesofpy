import os
import random
import string

import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    db = MovieDb(DB, DATA, TABLE)
    db.init()
    yield db
    db.drop_table()

# write tests for all MovieDb's query / add / delete
@pytest.mark.parametrize(
    "title, year, score_gt, expected",
    [
        ("The Godfather", None, None, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[0] == "The Godfather"]),
        (None, 1972, None, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[1] == 1972]),
        (None, None, 8.7, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[2] > 8.7]),
        (None, 1962, 8.3, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[1] == 1962]),
        ("Citizen Kane", None, 8.3, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[0] == "Citizen Kane"]),
        ("Citizen Kane", 1941, None, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[1] == 1941]),
        ("Citizen K", None, None, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[1] == 1941]),
        ("izen Kane", None, None, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[1] == 1941]),
        ("izen Kan", None, None, [(idx, e[0], e[1], e[2]) for idx, e in enumerate(DATA, start=1) if e[1] == 1941]),

    ],
)
def test_query(db, title, year, score_gt, expected):
    row = db.query(title, year, score_gt)
    assert row == expected


def test_add(db):
    rowid = db.add("The Matrix", 1999, 9.8)
    q = db.query("The Matrix")
    assert q == [(rowid, "The Matrix", 1999, 9.8)]


def test_delete(db):
    rowid = db.add("The Matrix", 1999, 9.8)
    db.delete(rowid)
    new_q = db.query("The Matrix")
    assert new_q == []