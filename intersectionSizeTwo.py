from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        prevStart, prevEnd = intervals[0][1] - 1, intervals[0][1]
        ans = 2
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval[0], interval[1]
            if start > prevEnd:
                ans += 2
                prevEnd = end
                prevStart = end - 1
            elif prevStart < start:
                if prevEnd == end:
                    prevEnd = end - 1
                else:
                    prevStart = end

                if prevStart > prevEnd:
                    prevStart, prevEnd = prevEnd, prevStart
                ans += 1
        return ans


sln = Solution()
print(
    sln.intersectionSizeTwo(
        [[8, 10], [2, 4], [4, 5]],
    )
)
