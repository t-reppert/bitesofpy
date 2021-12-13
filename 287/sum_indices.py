from typing import List
from collections import defaultdict
from copy import deepcopy

def sum_indices(items: List[str]) -> int:
    totals = []
    indexes = defaultdict(list)
    for idx,i in enumerate(items):
        prev_indexes = deepcopy(indexes[i])
        indexes[i].append(idx)
        totals.append(idx+sum(prev_indexes))     
    return sum(totals)