from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError
    new_list = []
    for num in numbers:
        length = len(str(abs(int(num))))
        if length < n:
            multiplier = 10**(n-1)
            num = int(num * multiplier)
        elif length > n:
            num = int(str(num)[:n])
        new_list.append(num)
    return new_list