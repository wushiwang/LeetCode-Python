#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (30.62%)
# Total Accepted:    11.4K
# Total Submissions: 37.3K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the
# ball, you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N
# times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 109 + 7.
#
# Example 1:
#
# Input:m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
#
#
#
#
# Example 2:
#
# Input:m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
#
#
#
#
# Note:
#
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
#


class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        self.MOD = int(1e9+7)
        self.dx = [0, 1, -1, 0]
        self.dy = [1, 0, 0, -1]
        dp = [[[-1 for _ in range(N+1)] for _ in range(n)] for _ in range(m)]
        self.DFS(i, j, N, dp, m, n)
        return dp[i][j][N]

    def DFS(self, x, y, N, dp, m, n):
        if N == 0:
            dp[x][y][N] = 0
            return 0
        if dp[x][y][N] != -1:
            return dp[x][y][N]
        res = 0
        for d in range(4):
            nx, ny = x+self.dx[d], y+self.dy[d]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                res += self.DFS(nx, ny, N-1, dp, m, n) % self.MOD
            else:
                res += 1
        dp[x][y][N] = res % self.MOD
        return res
