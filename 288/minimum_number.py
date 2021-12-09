from typing import List


def minimum_number(digits: List[int]) -> int:
    if digits:
        uniques = [str(x) for x in sorted(list(set(digits)))]
        return int(''.join(uniques))
    else:
        return 0
