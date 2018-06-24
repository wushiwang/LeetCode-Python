#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (38.01%)
# Total Accepted:    116.2K
# Total Submissions: 305.5K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
import math


class Solution:
    # Reuse _dp through solutions
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        for i in range(len(dp), n+1):
            cur = math.inf
            for j in range(1, math.floor(math.sqrt(i))+1):
                cur = min(cur, 1+dp[i-j*j])
            dp.append(cur)
        return dp[n]
