def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    textlist=text.split()
    non_ascii_words = []
    for word in textlist:
        for letter in word:
            if ord(letter) > 127:
                if word not in non_ascii_words:
                    non_ascii_words.append(word)
    return non_ascii_words


