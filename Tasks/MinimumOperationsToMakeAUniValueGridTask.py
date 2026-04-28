from typing import List

def minOperations(self, grid: List[List[int]], x: int) -> int:
    flat = []
    for row in grid:
        flat.extend(row)

    remainder = flat[0] % x
    for num in flat:
        if num % x != remainder:
            return -1

    flat.sort()
    n = len(flat)
    median = flat[n // 2]

    result = 0
    for num in flat:
        diff = abs(num - median)
        result += diff // x

    return result

#https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2026-04-28