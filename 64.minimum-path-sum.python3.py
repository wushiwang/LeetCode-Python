#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (41.29%)
# Total Accepted:    153.7K
# Total Submissions: 371.7K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for x in range(n)] for y in range(2)]
        for i in range(m):
            for j in range(n):
                c, d = i & 1, (i+1) & 1
                dp[c][j] = grid[i][j]
                if i >= 1 and j >= 1:
                    dp[c][j] += min(dp[d][j], dp[c][j-1])
                elif i >= 1:
                    dp[c][j] += dp[d][j]
                elif j >= 1:
                    dp[c][j] += dp[c][j-1]
        return dp[(m-1) & 1][n-1]
