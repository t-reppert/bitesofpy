import math
def binary_search(sequence, target):
    start = 0
    end = len(sequence) - 1
    while start <= end:
        middle = math.floor((start + end)/2)
        if sequence[middle] < target:
            start = middle + 1
        elif sequence[middle] > target:
            end = middle - 1
        else:
            return middle
    return None