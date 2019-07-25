def find_number_pairs(numbers, N=10):
    pairs = []
    pair_set = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == N and i != j:
                if tuple(sorted([ numbers[i], numbers[j] ])) not in pair_set:
                    pairs.append((numbers[i], numbers[j]))
                    pair_set.add(tuple(sorted([numbers[i], numbers[j]])))
    
    return pairs
