from typing import List


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """
    table = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            table[i] += table[i - coin]
    return table[-1]
