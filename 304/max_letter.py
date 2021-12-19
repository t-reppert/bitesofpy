from typing import Tuple
from collections import defaultdict, Counter
import re

def clean_word(word):
    cleaned = re.sub(r'[!#?,.:";_$]', '', word)
    cleaned = re.sub(r'\'$', '', cleaned)
    cleaned = re.sub(r'^\'', '', cleaned)
    return cleaned

def extra_clean_word(word):
    return re.sub(r'[!#?,.:";_\-\'$]', '', word)

def super_clean_word(word):
    new_word = re.sub(r'[!#?,.:";_0-9$\(\)]', '', word)
    new_word = clean_nonascii(new_word)
    return new_word

def clean_emoji(text):
    regex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regex_pattern.sub(r'',text)

def clean_nonascii(text):
    return re.sub(r'^[^\x00-\x7F]+','', text)

def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    if text is None or isinstance(text, (bool, int, float, list, dict)):
        raise ValueError
    s = re.sub('[%$0-9.\?#!,\n]', '', text.strip())
    s = clean_emoji(s)
    s = s.strip()
    if s == '':
        return ('', '', 0)
    words = s.split(' ')
    word_dict = defaultdict(dict)
    most_repeated = 0
    for word in words:
        if most_repeated == 0:
            most_repeated = 1
            word_dict[1] = {"word": word, "letter": word[0]}
        w = word.casefold().lower()
        count = Counter(extra_clean_word(w))
        for k,v in count.items():
            if v >= 2:
                if v > most_repeated:
                    most_repeated = v
                    word_dict[v] = {"word":clean_word(word), "letter":k}
    max_word = max(word_dict.keys())
    word = super_clean_word(word_dict[max_word]['word'])
    return (word, word_dict[max_word]['letter'], max_word)