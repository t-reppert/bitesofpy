import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    timestamp_regex = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}')
    if timestamp_regex.search(text):
        return True
    else:
        return False


def is_integer(number):
    """Return True if number is an integer"""
    if type(number) != int:
        return False
    else:
        return True


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    dashes = re.compile(r'([a-zA-Z0-9]-[a-zA-Z0-9])+')
    if dashes.search(text):
        return True
    else:
        return False

def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    regex = r' \([a-zA-Z0-9\.]+\)'
    return re.sub(regex,'',text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    splitlist = re.split(r'[?!\.,;] *',text)
    splitlist = list(filter(None,splitlist))
    return splitlist


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r' +',' ',text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    vowels = re.compile(r'[aeiou]{3}',re.I)
    if vowels.search(word):
        return True
    else:
        return False


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    date_format = re.compile(r'([0-9]{2})/([0-9]{2})/([0-9]{4})')
    if date_format.match(date):
        dd = date_format.match(date).group(1)
        mm = date_format.match(date).group(2)
        yy = date_format.match(date).group(3)
        return mm + "/" + dd + "/" + yy
    else:
        return date

