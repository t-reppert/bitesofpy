from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    letters = set(word.upper())
    if letters.intersection(LEFT_HAND_CHARS) and letters.intersection(RIGHT_HAND_CHARS):
        return Hand.BOTH
    elif letters.intersection(LEFT_HAND_CHARS) and not letters.intersection(RIGHT_HAND_CHARS):
        return Hand.LEFT
    elif not letters.intersection(LEFT_HAND_CHARS) and letters.intersection(RIGHT_HAND_CHARS):
        return Hand.RIGHT

