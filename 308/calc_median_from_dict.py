import numpy as np

def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    minimum = min(d.values())
    maximum = False
    for k, v in d.items():
        if v > minimum and v > 1_000_000_000_000:
            maximum = max(d.values())
    if not maximum:
        d = {k: v//minimum for k, v in d.items()}
    else:
        new_d = {}
        for k,v in d.items():
            if v >= maximum:
                new_d[k] = v//maximum
            else:
                new_d[k] = v
        d = new_d
    new_list = [k for k,v in d.items() for i in range(int(v))]
    return np.median(new_list)
