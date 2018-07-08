#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (41.78%)
# Total Accepted:    61.1K
# Total Submissions: 146.4K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        L, R = len(num1)-1, len(num2)-1
        add, res = 0, ""
        while not (L < 0 and R < 0):
            if L < 0:
                cur = add + int(num2[R])
                R -= 1
            elif R < 0:
                cur = add + int(num1[L])
                L -= 1
            else:
                cur = add + int(num1[L]) + int(num2[R])
                L, R = L-1, R-1
            if cur >= 10:
                cur -= 10
                add = 1
            else:
                add = 0
            res += str(cur)
        if add == 1:
            res += str(add)
        return res[::-1]
