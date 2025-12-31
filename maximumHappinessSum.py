from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        reduced = 0
        i = len(happiness) - 1
        while i >= 0 and k > 0:
            if happiness[i] - reduced <= 0:
                break
            ans += happiness[i] - reduced
            reduced += 1
            i -= 1
            k -= 1
        return ans


sln = Solution()

print(sln.maximumHappinessSum([1, 2, 3], 2))
