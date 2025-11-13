from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_max = [0] * n
        prefix_max[0] = nums[0]
        suffix_max[n - 1] = nums[n - 1]
        ans = 0
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
            suffix_max[n - 1 - i] = max(suffix_max[n - i], nums[n - 1 - i])
        return ans


sln = Solution()
sln.maximumTripletValue([12, 6, 1, 2, 7])
