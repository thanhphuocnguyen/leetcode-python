import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        priority_queue = []
        # initialize boundaries
        for i in range(m):
            heapq.heappush(
                priority_queue,
                (
                    heightMap[i][0],
                    i,
                    0,
                ),
            )
            visited[i][0] = True

            heapq.heappush(
                priority_queue,
                (
                    heightMap[i][n - 1],
                    i,
                    n - 1,
                ),
            )
            visited[i][n - 1] = True

        for j in range(n):
            heapq.heappush(
                priority_queue,
                (
                    heightMap[0][j],
                    0,
                    j,
                ),
            )
            visited[0][j] = True

            heapq.heappush(priority_queue, (heightMap[m - 1][j], m - 1, j))
            visited[m - 1][j] = True

        ans = 0
        while priority_queue:
            cell = heapq.heappop(priority_queue)
            h, currRow, currCol = cell
            for dir in directions:
                nextRow, nextCol = currRow + dir[0], currCol + dir[1]
                if (
                    self.isValid(nextRow, nextCol, m, n)
                    and not visited[nextRow][nextCol]
                ):
                    nextH = heightMap[nextRow][nextCol]
                    visited[nextRow][nextCol] = True
                    if nextH < h:
                        ans += h - nextH
                    heapq.heappush(priority_queue, (max(nextH, h), nextRow, nextCol))

        return ans

    def isValid(self, i, j, m, n):
        return i >= 0 and j >= 0 and i < m and j < n


sln = Solution()
print(sln.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
