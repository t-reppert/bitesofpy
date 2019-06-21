from itertools import cycle
from string import ascii_uppercase
def sequence_generator():
    count = list(range(1,27))
    letters = list(ascii_uppercase)
    sequence = [seq for pair in zip(count, letters) for seq in pair]
    return cycle(sequence)