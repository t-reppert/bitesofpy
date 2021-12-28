from typing import List


def pascal(n: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    p = [[1], [1,1], [1,2,1]]
    if n == 0:
        return []
    if n == 1 or n == 2 or n == 3:
        return p[n-1]
    count = 3
    prev_row = p[count-1]
    while count < n:
        new_row = [1]
        for i in range(0, len(prev_row)-1):
            new_row.append(prev_row[i]+prev_row[i+1])
        new_row.append(1)
        p.append(new_row)
        count += 1
        prev_row = new_row
    return p[n-1]