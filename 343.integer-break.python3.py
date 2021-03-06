#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (46.65%)
# Total Accepted:    60.1K
# Total Submissions: 128.9K
# Testcase Example:  '2'
#
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
#
#
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 =
# 3 + 3 + 4).
#
#
#
# Note: You may assume that n is not less than 2 and not larger than 58.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], j*max(i-j, dp[i-j]))
        return dp[n]
