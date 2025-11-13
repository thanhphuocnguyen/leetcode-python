from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        flatten = [0] * (m * n)
        for i in range(0, m):
            for j in range(0, n):
                flatten[i * n + j] = grid[i][j]

        median = flatten[m * n // 2]

        ans = 0
        for num in flatten:
            if abs(num - median) % x != 0:
                return -1
            ans += abs(num - median) // x
        return ans
