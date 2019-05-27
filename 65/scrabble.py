import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    perms = _get_permutations_draw(draw)
    wordlist = set()

    for word in list(dictionary):
        if len(word) > 1 and len(word) < len(draw):
            for letterlist in perms:
                if word in letterlist and word not in wordlist:
                    wordlist.add(word)
    return wordlist

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    lol = ''.join(draw)
    return [ ''.join(x).lower() for x in itertools.permutations(lol) ]


