from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        mat = [[0 for _ in range(n)] for _ in range(m)]

        # guard cell will be 2, wall cell will be 3
        for g in guards:
            r, c = g[0], g[1]
            mat[r][c] = 2
        for w in walls:
            r, c = w[0], w[1]
            mat[r][c] = 3

        for g in guards:
            r, c = g[0], g[1]
            i, j = r - 1, c - 1
            while i >= 0 and mat[i][c] != 2 and mat[i][c] != 3:
                mat[i][c] = 1
                i -= 1
            while j >= 0 and mat[r][j] != 2 and mat[r][j] != 3:
                mat[r][j] = 1
                j -= 1
            i, j = r + 1, c + 1
            while i < m and mat[i][c] != 2 and mat[i][c] != 3:
                mat[i][c] = 1
                i += 1
            while j < n and mat[r][j] != 2 and mat[r][j] != 3:
                mat[r][j] = 1
                j += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans += 1
        return ans


sln = Solution()
print(sln.countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]))
