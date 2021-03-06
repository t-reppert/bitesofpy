from dataclasses import dataclass, field
from typing import List, Tuple
import heapq

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __str__(self):
        return f'[{self.bites}] {self.name}'


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    rankings: list = field(default_factory=list)

    def add(self, ninja):
        self.rankings.append(ninja)
    
    def dump(self):
        max = sorted(self.rankings,key=lambda x:x.bites,reverse=True)
        dumped = max.pop()
        self.rankings = max
        return dumped

    def highest(self,count=1):
        return sorted(self.rankings,key=lambda x:x.bites,reverse=True)[:count]

    def lowest(self,count=1):
        return sorted(self.rankings,key=lambda x:x.bites)[:count]

    def pair_up(self,count=3):
        return list(zip(self.highest(count),self.lowest(count)))
    
    def __len__(self):
        return len(self.rankings)
    
    



    