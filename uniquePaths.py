from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(memo, 0, 0, m, n)

    def dp(self, memo: List[List[int]], i: int, j: int, m: int, n: int) -> int:
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if memo[i][j] != -1:
            return memo[i][j]
        down = self.dp(memo, i + 1, j, m, n)
        right = self.dp(memo, i, j + 1, m, n)
        memo[i][j] = down + right
        return memo[i][j]


sln = Solution()

print(sln.uniquePaths(3, 7))
