#
# [629] K Inverse Pairs Array
#
# https://leetcode.com/problems/k-inverse-pairs-array/description/
#
# algorithms
# Hard (27.79%)
# Total Accepted:    5.6K
# Total Submissions: 20.2K
# Testcase Example:  '3\n0'
#
#
# Given two integers n and k, find how many different arrays consist of numbers
# from 1 to n such that there are exactly k inverse pairs.
#
#
# We define an inverse pair as following:
# For ith and jth element in the array, if i < j and a[i] > a[j] then it's an
# inverse pair; Otherwise, it's not.
#
#
#
# Since the answer may be very large, the answer should be modulo 109 + 7.
#
#
# Example 1:
#
# Input: n = 3, k = 0
# Output: 1
# Explanation:
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0
# inverse pair.
#
#
#
# Example 2:
#
# Input: n = 3, k = 1
# Output: 2
# Explanation:
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
#
#
#
# Note:
#
# The integer n is in the range [1, 1000] and k is in the range [0, 1000].
#


class Solution:
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1
        if n == 0:
            return 0
        MOD = 1000000007
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[1][0] = 1
        for i in range(2, n+1):
            s, L = 0, 0
            for j in range(k+1):
                s += dp[i-1][j]
                s %= MOD
                if L < j-i+1:
                    s -= dp[i-1][L]
                    L += 1
                dp[i][j] = s
        #print(dp)
        return dp[n][k]
