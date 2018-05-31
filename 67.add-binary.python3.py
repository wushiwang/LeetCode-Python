#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (34.44%)
# Total Accepted:    206K
# Total Submissions: 597K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a), len(b)
        if m == 0 and n == 0:
            return ""
        if n == 0:
            return a
        if m == 0:
            return b
        i, j, res, add = m-1, n-1, list(), 0
        while not (i == -1 and j == -1):
            tmp, add = add, 0
            if i != -1:
                tmp += int(a[i])
                i -= 1
            if j != -1:
                tmp += int(b[j])
                j -= 1
            if tmp >= 2:
                tmp, add = tmp-2, 1
            res = [str(tmp)] + res
        if add == 1:
            res = ['1'] + res

        return ''.join(res)
