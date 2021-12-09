from collections import Counter

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    counts = Counter(numbers)
    major = max(counts.keys(), key=(lambda k:counts[k]))
    minor = min(counts.keys(), key=(lambda k:counts[k]))
    
    return major, minor