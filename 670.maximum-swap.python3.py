# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (38.82%)
# Total Accepted:    25.5K
# Total Submissions: 65.7K
# Testcase Example:  '2736'
#
#
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
#
#
# Example 1:
#
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
#
# Example 2:
#
# Input: 9973
# Output: 9973
# Explanation: No swap.
#
#
#
#
# Note:
#
# The given number is in the range [0, 108]
#


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        dp = [None]*len(num)
        maxx, pos = -1, None
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) > maxx:
                maxx, pos = int(num[i]), i
            dp[i] = (maxx, pos)
        for i in range(len(num)-1):
            if dp[i+1][0] > int(num[i]):
                tmp = num[i]
                num[i] = str(dp[i+1][0])
                num[dp[i+1][1]] = tmp
                return int(''.join(num))
        return int(''.join(num))
