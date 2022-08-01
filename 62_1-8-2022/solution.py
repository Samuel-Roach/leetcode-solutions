class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * m] * n
        for i in range(0, m):
            paths[0][i] = 1
        for i in range(0, n):
            paths[i][0] = 1
        for j in range(1, n):
            for i in range(1, m):
                paths[j][i] = paths[j-1][i] + paths[j][i-1]

        return paths[n-1][m-1]