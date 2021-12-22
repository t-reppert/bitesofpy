IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    def is_neg(val):
        if val < 0:
            return True
        else:
            return False
    if all([is_neg(v) for v in village]):
        print(IMPOSSIBLE)
        return (0,0,0)
    pos_indexes = []
    for idx, x in enumerate(village):
        if x > 0:
            pos_indexes.append(idx)
    if len(pos_indexes) == 1:
        return (village[pos_indexes[0]], pos_indexes[0]+1, pos_indexes[0]+1)
    temp_max = 0
    max_start = 0
    max_end = 0
    for p in pos_indexes:
        for i in range(p+1, pos_indexes[-1] + 2):
            s = sum(village[p:i])
            if s > temp_max:
                temp_max = s
                max_start = p
                max_end = i
        for v in pos_indexes:
            if village[v] > temp_max:
                temp_max = village[v]
                max_start = v
                max_end = v
            
    return (temp_max, max_start+1, max_end)
