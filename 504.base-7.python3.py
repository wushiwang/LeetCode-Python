#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (43.92%)
# Total Accepted:    30.5K
# Total Submissions: 69.4K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
#
#
# Example 2:
#
# Input: -7
# Output: "-10"
#
#
#
# Note:
# The input will be in range of [-1e7, 1e7].
#


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        neg = False
        if num < 0:
            num *= -1
            neg = True
        res = ''
        while num != 0:
            res += str(num%7)
            num //= 7
        if neg:
            return '-'+res[::-1]
        else:
            return res[::-1]
