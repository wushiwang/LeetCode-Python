#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (34.61%)
# Total Accepted:    67.1K
# Total Submissions: 193.8K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
#
# Example 1:
#
#
# Input: [5,7]
# Output: 4
#
#
# Example 2:
#
#
# Input: [0,1]
# Output: 0
#


class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = i = 0
        while n != m:
            res <<= 1
            n >>= 1
            m >>= 1
            i += 1
        return res | (n << i)
