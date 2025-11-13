from typing import Counter, List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            ones, zeros = 0, 0
            for c in s:
                if c == "1":
                    ones += 1
                else:
                    zeros += 1
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]


sln = Solution()
print(sln.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
