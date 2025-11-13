from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                ans+= min(neededTime[i],neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        return ans


sln = Solution()
print(sln.minCost("abaac", [1, 2, 3, 4, 5]))
print(sln.minCost("cddcdcae", [4, 8, 8, 4, 4, 5, 4, 2]))
