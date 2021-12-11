import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    s = [set(a) for a in args if a]
    if not s:
        return set()
    x = s[1:]
    return s[0].intersection(*x)