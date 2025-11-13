from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)

        cnt = 0
        for i in range(0, 3):
            for j in range(cnt, cnt + freq[i]):
                nums[j] = i
            cnt += freq[i]


sln = Solution()
sln.sortColors([2, 0, 2, 1, 1, 0])
