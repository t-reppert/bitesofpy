from typing import List, NamedTuple
from collections import namedtuple
from textblob import Word

MIN_CONFIDENCE = 0.5


# define SuggestedWord NamedTuple with attributes
# word (str) and confidence (float)
SuggestedWord = namedtuple("SuggestedWord", ["word", "confidence"])


def get_spelling_suggestions(
    word: str, min_confidence: float = MIN_CONFIDENCE
) -> List[SuggestedWord]:
    """
    Find spelling suggestions with at least minimum confidence score
    Use textblob.Word (check out the docs)
    """
    return [w for w in Word(word).spellcheck() if w[1] >= min_confidence]

