from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    result = []
    if not buildings:
        return []
    if len(buildings) == 1:
        return [0]
    if direction == 'W':
        for i in range(0, len(buildings)):
            if i  == 0:
                result.append(i)
                prev_high = buildings[i]
            else:
                if buildings[i] > prev_high:
                    result.append(i)
                    prev_high = buildings[i]
        return result
    elif direction == 'E':
        prev_high = buildings[-1]
        for i in range(len(buildings)-1, -1, -1):
            if i == len(buildings)-1:
                result.append(i)
            else:
                print(i)
                if buildings[i] > prev_high:
                    result.append(i)
                    prev_high = buildings[i]
        
        return list(reversed(result))
    else:
        return []

if __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]