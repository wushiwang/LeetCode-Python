#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (31.94%)
# Total Accepted:    6.3K
# Total Submissions: 19.9K
# Testcase Example:  '1'
#
# Given a positive integer n, find the number of non-negative integers less
# than or equal to n, whose binary representations do NOT contain consecutive
# ones.
#
# Example 1:
#
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers
#
#
# Note:
# 1 9
#


class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [0]*(32)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 32):
            dp[i] = dp[i-1] + dp[i-2]
        res, k, pre = 0, 30, 0
        while k >= 0:
            if (1 << k) & num != 0:
                res += dp[k]
                if pre == 1:
                    return res
                pre = 1
            else:
                pre = 0
            k -= 1
        return res+1
