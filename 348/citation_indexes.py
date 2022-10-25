from typing import Sequence
from collections import defaultdict

TYPE_ERROR_MSG = "Unsupported input type: use either a list or a tuple"
VALUE_ERROR_MSG = "Unsupported input value: citations cannot be neither empty nor None"

def check_citations(citations):
    if citations is None:
        raise ValueError(VALUE_ERROR_MSG)
    if not isinstance(citations, (list, tuple)):
        raise TypeError(TYPE_ERROR_MSG)
    elif len(citations) == 0:
        raise ValueError(VALUE_ERROR_MSG)
    else:
        for i in citations:
            if not isinstance(i, int):
                raise ValueError(VALUE_ERROR_MSG)
            elif i < 0:
                raise ValueError(VALUE_ERROR_MSG)


def h_index(citations: Sequence[int]) -> int:
    """Return the highest number of papers h having at least h citations"""
    check_citations(citations)
    paper_count = len(citations)
    counts = defaultdict(int)
    for i in range(1, paper_count+1):
        for j in range(paper_count):
            if citations[j] >= i:
                counts[i] += 1
    for k, v in counts.items():
        if k == v:
            return k
    if len(counts) == 1 and 1 in counts:
        if counts[1] >= 1:
            return 1
    return 0


def i10_index(citations: Sequence[int]) -> int:
    """Return the number of papers having at least 10 citations"""
    check_citations(citations)
    paper_count = len(citations)
    count = 0
    for i in range(paper_count):
        if citations[i] >= 10:
            count += 1
    return count

