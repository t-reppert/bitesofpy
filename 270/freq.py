from collections import Counter

def freq_digit(num: int) -> int:
    digits = [x for x in str(num)]
    counts = Counter(digits)
    values = {}
    for k, v in counts.items():
        if v in values:
            values[v] += 1
        else:
            values[v] = 1
    if len(values) == 1:
        return int(digits[0])
    return int(counts.most_common(1)[0][0])
