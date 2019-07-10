def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    target_pairs = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target:
                if numbers[i] < numbers[j]:
                    target_pairs.append((i, j))

    if len(target_pairs) > 1:
        return sorted(target_pairs, key=lambda x:numbers[x[0]])[0]
    elif len(target_pairs) == 1:
        return target_pairs[0]
    else:
        return None