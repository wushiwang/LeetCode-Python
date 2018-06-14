#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (18.23%)
# Total Accepted:    66.7K
# Total Submissions: 365.4K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# Example 1:
#
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
#
# Example 2:
#
#
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
#
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
#


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = True if numerator*denominator < 0 else False
        numerator = int(abs(numerator))
        denominator = int(abs(denominator))
        L = "-" if flag else ""
        L += str(numerator // denominator)
        numerator %= denominator
        if numerator == 0:
            return L
        cur, dic, R, pos = numerator*10, dict(), "", -1
        while True:
            if cur in dic:
                pos = dic[cur]
                return L + '.' + R[:pos] + "(" + R[pos:] + ")"
            dic[cur] = len(R)
            R += str(cur // denominator)
            cur %= denominator
            cur *= 10
            if cur == 0:
                return L + '.' + R
