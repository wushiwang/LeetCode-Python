#
# [440] K-th Smallest in Lexicographical Order
#
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (25.84%)
# Total Accepted:    6.4K
# Total Submissions: 24.8K
# Testcase Example:  '13\n2'
#
# Given integers n and k, find the lexicographically k-th smallest integer in
# the range from 1 to n.
#
# Note: 1 ≤ k ≤ n ≤ 109.
#
# Example:
#
# Input:
# n: 13   k: 2
#
# Output:
# 10
#
# Explanation:
# The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so
# the second smallest number is 10.
#


class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res, k = 1, k - 1
        while k != 0:
            cnt = 0
            L, R = res, res+1
            while L <= n:
                cnt += min(n+1, R) - L
                L, R = L*10, R*10
            if cnt <= k:
                k -= cnt
                res += 1
            else:
                res *= 10
                k -= 1
        return res

