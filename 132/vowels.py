VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    max_v_count = 0
    max_word = ""
    for t in text.split():
        v_count = 0
        for c in t:
            if c in VOWELS:
                v_count += 1
        if v_count > max_v_count:
            max_v_count = v_count
            max_word = (t.lower(), v_count)
    return max_word
        


