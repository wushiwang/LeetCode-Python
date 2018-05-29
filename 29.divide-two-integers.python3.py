#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (15.72%)
# Total Accepted:    135.5K
# Total Submissions: 862.1K
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
#
# Note:
#
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 231 − 1 when the division
# result overflows.
#


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = False
        if (dividend > 0 and divisor < 0) or\
                (dividend < 0 and divisor > 0):
            flag = True
        dividend, divisor = abs(dividend), abs(divisor)
        res, tmp = 0, 0
        while (divisor << tmp) <= dividend:
            tmp = tmp + 1
        tmp = tmp - 1
        while dividend >= divisor:
            while (divisor << tmp) > dividend:
                tmp = tmp - 1
            res += (1 << tmp)
            dividend -= (divisor << tmp)
            tmp = tmp - 1

        res = -res if flag else res
        if res < -(2**31) or res > (2**31)-1:
            return (2**31)-1
        return res
