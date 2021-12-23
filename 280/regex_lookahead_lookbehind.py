import re


def count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """
    patt = r"([\d\D])(?=" + n*r"\1" + r")"
    matches = re.finditer(patt, text, re.MULTILINE)
    return len([x for x in matches])

def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    if n == 1 and char:
        n_string = r""
    else:
        n_string = n*r"\1"
    if not char:
        c = re.escape(char)
        patt = r"([\d\D.\w\W\n\.])(?=("+n*r"\1"+r"))"
    else:
        c = re.escape(char)
        if n == 1:
            z = 0
        else:
            z = 1
        patt = r"([\d\D\w\W\.\n])(?="+z*r"\1" +r"(\1"+r"|"+c+r"))"        
    matches = re.finditer(patt, text, re.MULTILINE)
    return len([x for x in matches])

def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    escaped = [re.escape(c) for c in surrounding_chars]
    c = '|'.join(escaped)
    patt = r"(?<=" + c + r")([\d\D.\w\W])(?=" + c + r")"
    matches = re.finditer(patt, text, re.MULTILINE)
    return len([x for x in matches])