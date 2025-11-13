import heapq
import sys
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        n, m = len(moveTime), len(moveTime[0])
        dst = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        pq = []
        heapq.heappush(pq, (0, [0, 0, 1]))
        dst[0][0] = 0

        while len(pq) > 0:
            _, val = heapq.heappop(pq)
            currRow, currCol, move = val[0], val[1], val[2]
            if visited[currRow][currCol]:
                continue
            visited[currRow][currCol] = True
            for dir in directions:
                rowMove, colMove = dir[0], dir[1]
                nextRow, nextCol = currRow + rowMove, currCol + colMove
                if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= m:
                    continue
                moveTimeToNextCell = (
                    max(moveTime[nextRow][nextCol], dst[currRow][currCol]) + move
                )
                if moveTimeToNextCell < dst[nextRow][nextCol]:
                    dst[nextRow][nextCol] = moveTimeToNextCell
                    heapq.heappush(
                        pq,
                        (moveTimeToNextCell, [nextRow, nextCol, 1 if move == 2 else 2]),
                    )
        return dst[n - 1][m - 1]


sln = Solution()
print(sln.minTimeToReach([[0, 4], [4, 4]]))  # Output: 4
print(sln.minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]]))  # Output: 4
print(sln.minTimeToReach([[0, 1], [1, 2]]))  # Output: 4
