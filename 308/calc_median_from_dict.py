def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    running_total = 0
    sum_counts = sum(d.values())
    average = sum_counts / 2
    equal_check = sum(d.values()) / len(d)
    if len(d) % 2 == 0 and all([v == equal_check for v in d.values()]):
        return sum(d.keys()) / 2
    prev_run_total = 0
    for num, count in sorted(d.items()):
        running_total = count + prev_run_total
        if average <= running_total and average > prev_run_total:
            return num
        prev_run_total = running_total
