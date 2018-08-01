#
# [634] Find the Derangement of An Array
#
# https://leetcode.com/problems/find-the-derangement-of-an-array/description/
#
# algorithms
# Medium (36.25%)
# Total Accepted:    3.7K
# Total Submissions: 10.3K
# Testcase Example:  '1'
#
#
# In combinatorial mathematics, a derangement is a permutation of the elements
# of a set, such that no element appears in its original position.
#
#
#
# There's originally an array consisting of n integers from 1 to n in ascending
# order, you need to find the number of derangement it can generate.
#
#
#
# Also, since the answer may be very large, you should return the output mod
# 109 + 7.
#
#
# Example 1:
#
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1]
# and [3,1,2].
#
#
#
# Note:
# n is in the range of [1, 106].
#
#
class Solution:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        MOD = 1000000007
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = ((i-1) * (dp[i-1] + dp[i-2])) % MOD
        return dp[n]
