from enum import Enum
from statistics import mean
THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return '{0} => {1}'.format(self.name,THUMBS_UP*self.value)

    @classmethod
    def average(cls):
        return mean([e.value for e in Score])