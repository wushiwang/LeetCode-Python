#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (45.44%)
# Total Accepted:    22.2K
# Total Submissions: 48.8K
# Testcase Example:  '3'
#
#
# Initially on a notepad only one character 'A' is present. You can perform two
# operations on this notepad for each step:
#
# Copy All: You can copy all the characters present on the notepad (partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
#
#
#
#
# Given a number n. You have to get exactly n 'A' on the notepad by performing
# the minimum number of steps permitted. Output the minimum number of steps to
# get n 'A'.
#
#
# Example 1:
#
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#
#
#
#
# Note:
#
# The n will be in the range [1, 1000].
#
import math


class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [math.inf]*(n+1)
        dp[1] = 0
        for i in range(2, n+1):
            for j in range((n >> 1), 0, -1):
                if i % j == 0 and dp[j] != math.inf:
                    dp[i] = min(dp[i], dp[j] + i // j)
                    break
        return dp[n]
