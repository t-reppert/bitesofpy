from collections import deque

def num_ops(target):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    cache = []
    calc = 1
    ops = 0
    log = deque([(ops, calc)])
    safe_limit = target * 15
    while log:
        ops, calc = log.popleft()
        if calc == target:
            break
        ops += 1
        if (calc * 2) not in cache and calc < safe_limit:
            new_calc = calc * 2
            log.append((ops, new_calc))
            cache.append(new_calc)
        if (calc // 3) not in cache:
            new_calc = calc // 3
            log.append((ops, new_calc))
            cache.append(new_calc)
    return ops