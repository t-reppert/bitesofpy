from typing import List
from itertools import zip_longest

def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    joined = []
    for l in lst_of_lst:
        temp = ""
        for z in l:
            temp += str(z)
        joined.append(temp)
    z = zip_longest(*joined, fillvalue=fillvalue)
    filled_z = zip(*z)
    unzipped_list = list(filled_z)
    final = []
    for l in unzipped_list:
        t = [int(i) for i in l]
        final.append(t)
    return final