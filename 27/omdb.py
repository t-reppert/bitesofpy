import glob
import json
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))

def get_movie_data(files=files):
    movies = []
    for file in files:
        movies.append(json.load(open(file, 'r')))
    return movies

def get_single_comedy(movies):
    for movie in movies:
        if "Comedy" in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies):
    nomination_regex = re.compile(r' (\d+) nominations.')
    nomination_list = []
    for movie in movies:
        nominations = int(nomination_regex.search(movie['Awards']).group(1))
        nomination_list.append((movie['Title'],nominations))
    return max(nomination_list,key=lambda x:x[1])[0]


def get_movie_longest_runtime(movies):
    runtime_list = []
    for movie in movies:
        runtime = int(movie['Runtime'].replace(' min',''))
        runtime_list.append((movie['Title'],runtime))
    return max(runtime_list,key=lambda x:x[1])[0]



