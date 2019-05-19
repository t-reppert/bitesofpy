import unicodedata


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in text string
    """
    return sorted(set([ x.lower() for x in text if 'WITH' in unicodedata.name(x) ]))

