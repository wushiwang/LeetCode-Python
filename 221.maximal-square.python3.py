#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (30.64%)
# Total Accepted:    91.4K
# Total Submissions: 298K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],
# ["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        dp = [[0 for x in range(len(matrix[0]))] for y in range(2)]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i&1][j] = int(matrix[i][j])
                if i != 0 and j != 0:
                    if matrix[i][j] == "1":
                        dp[i&1][j] = max(int(matrix[i][j]), min(dp[(i+1)&1][j-1], dp[i&1][j-1], dp[(i+1)&1][j])+1)
                res = max(res, dp[i&1][j])
        return res**2
