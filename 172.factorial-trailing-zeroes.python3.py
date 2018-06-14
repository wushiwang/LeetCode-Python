#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.02%)
# Total Accepted:    120.9K
# Total Submissions: 326.4K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.
#


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Count numbers of 5
        # Case 1: 5 came from n//5
        # Case 2: 5 came from n//5//5
        # and so on ..
        res = 0
        while n != 0:
            res += n // 5
            n //= 5
        return res
