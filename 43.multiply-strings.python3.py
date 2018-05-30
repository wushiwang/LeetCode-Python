#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (28.14%)
# Total Accepted:    140.6K
# Total Submissions: 499.3K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Example 1:
#
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Note:
#
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = ""
        for i in range(len(num2)-1, -1, -1):
            res = self.add(res, self.mult(num1, int(num2[i]), len(num2)-1-i))
        return res

    def mult(self, num1, n, p):
        if n == 0:
            return "0"
        res, add = "", 0
        for i in range(len(num1)-1, -1, -1):
            cur, add = add, 0
            cur += int(num1[i])*n
            cur, add = cur % 10, cur // 10
            res = str(cur) + res
        if add != 0:
            res = str(add) + res
        for i in range(p):
            res += "0"
        return res

    def add(self, num1, num2):
        i, j, res = len(num1)-1, len(num2)-1, ""
        add = 0
        while i >= 0 or j >= 0:
            sum, add = add, 0
            if i >= 0:
                sum += int(num1[i])
                i -= 1
            if j >= 0:
                sum += int(num2[j])
                j -= 1
            if sum >= 10:
                sum, add = sum-10, 1
            res = str(sum) + res
        if add == 1:
            res = "1" + res
        return res
