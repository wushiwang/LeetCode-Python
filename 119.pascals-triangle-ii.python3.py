#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (38.67%)
# Total Accepted:    149.1K
# Total Submissions: 385.4K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [[1 for x in range(rowIndex+1)] for y in range(2)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                dp[i&1][j] = dp[(i+1)&1][j] + dp[(i+1)&1][j-1]
        return dp[rowIndex&1]
