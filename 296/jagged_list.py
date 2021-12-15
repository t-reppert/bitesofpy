from typing import List
from itertools import zip_longest

def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    z = zip_longest(*lst_of_lst, fillvalue=fillvalue)
    return [list(l) for l in zip(*z)]
