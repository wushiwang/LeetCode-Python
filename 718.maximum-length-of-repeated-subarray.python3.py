#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (42.04%)
# Total Accepted:    17.2K
# Total Submissions: 40.9K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
#
# Example 1:
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#
# Note:
#
# 1
# 0
#


class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]
        res = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    res = max(res, dp[i][j])
        return res
