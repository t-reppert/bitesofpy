import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return 'Not found'


def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    emojis = {}
    for i in range(START_EMOJI_RANGE, sys.maxunicode + 1):
        try:
            emojis[chr(i)] = unicodedata.name(chr(i)).lower()
        except ValueError:
            pass
    return emojis

def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()

    emoji_mapping = _make_emoji_mapping()
    max_name_width = 0
    emoji_list = {}
    for emoji, name in emoji_mapping.items():
        if term.lower() in name.lower():
            if len(name) > max_name_width:
                max_name_width = len(name)
            emoji_list[name.strip()] = emoji.strip()
    if len(emoji_list) == 0:
        print("no matches")
    else:
        for name, emoji in emoji_list.items():
            print(f'{name.title(): <{max_name_width}} | {emoji}')
