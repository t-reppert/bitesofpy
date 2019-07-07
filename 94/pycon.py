from collections import namedtuple
import os
import pickle
import urllib.request
import re

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = 'http://projects.bobbelderbos.com/pcc/{}'.format(pkl_file)
pycon_videos = os.path.join('/tmp', pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos,'rb') as f:
        data = pickle.load(f)
    return data


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(videos, key=lambda kv: int(kv.metrics['viewCount']), reverse=True)


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    return sorted(videos, key=lambda kv: (int(kv.metrics['likeCount']) - int(kv.metrics['dislikeCount']))/int(kv.metrics['viewCount']), reverse=True)

def _duration_in_seconds(duration):
    sec_rx = re.compile(r'(\d+)S')
    min_rx = re.compile(r'(\d+)M')
    hour_rx = re.compile(r'(\d+)H')
    seconds = 0
    if 'H' in duration and hour_rx.search(duration):
        seconds += int(hour_rx.search(duration).group(1)) * 60 * 60
    if 'M' in duration and min_rx.search(duration):
        seconds += int(min_rx.search(duration).group(1)) * 60
    if 'S' in duration and sec_rx.search(duration):
        seconds += int(sec_rx.search(duration).group(1))
    return seconds    

def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return list(filter(lambda kv:_duration_in_seconds(kv.duration)>(60*60), videos))


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    return list(filter(lambda kv:_duration_in_seconds(kv.duration)<(24*60), videos))

