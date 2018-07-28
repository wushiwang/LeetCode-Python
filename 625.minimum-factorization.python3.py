#
# [625] Minimum Factorization
#
# https://leetcode.com/problems/minimum-factorization/description/
#
# algorithms
# Medium (31.31%)
# Total Accepted:    5K
# Total Submissions: 16.1K
# Testcase Example:  '48'
#
# Given a positive integer a, find the smallest positive integer b whose
# multiplication of each digit equals to a.
#
#
# If there is no answer or the answer is not fit in 32-bit signed integer, then
# return 0.
#
#
# Example 1
# Input:
# 48
# Output:
# 68
#
#
#
# Example 2
# Input:
# 15
#
# Output:
# 35
#


class Solution:
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return 1
        res = []
        for i in range(9, 1, -1):
            while a % i == 0:
                res.append(str(i))
                a /= i
        if a != 1:
            return 0
        res = sorted(res)
        res = int(''.join(res))
        if res > 2**31-1:
            return 0
        return res
