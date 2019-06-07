def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1 = sorted(word1.replace(' ','').lower())
    word2 = sorted(word2.replace(' ','').lower())
    if word1 == word2:
        return True
    return False

