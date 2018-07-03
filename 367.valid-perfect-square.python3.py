#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (38.77%)
# Total Accepted:    76.9K
# Total Submissions: 198.3K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
#
#
# Note: Do not use any built-in library function such as sqrt.
#
#
# Example 1:
#
# Input: 16
# Returns: True
#
#
#
# Example 2:
#
# Input: 14
# Returns: False
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        L, R = 1, num
        while L < R - 1:
            M = (L+R) >> 1
            if M*M > num:
                R = M
            elif M*M <= num:
                L = M
        return L*L == num
