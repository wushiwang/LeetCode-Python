#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (30.44%)
# Total Accepted:    68.4K
# Total Submissions: 224.6K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
#
# Example 1:
#
#
# Input: "3+2*2"
# Output: 7
#
#
# Example 2:
#
#
# Input: " 3/2 "
# Output: 1
#
# Example 3:
#
#
# Input: " 3+5 / 2 "
# Output: 5
#
#
# Note:
#
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
#


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr, i = [], 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                j = i+1
                while j < len(s) and ord(s[j]) >= ord('0') and ord(s[j]) <= ord('9'):
                    j += 1
                arr.append(int(s[i:j]))
                i = j-1
            else:
                arr.append(s[i])
            i += 1
        # Calculate * and /
        arr2, i = [], 0
        while i < len(arr):
            if arr[i] == '*':
                a = arr2.pop()
                arr2.append(a*arr[i+1])
                i += 1
            elif arr[i] == '/':
                a = arr2.pop()
                arr2.append(a//arr[i+1])
                i += 1
            else:
                arr2.append(arr[i])
            i += 1
        # Calculate + and -
        i, res, add, sub = 0, 0, False, False
        while i < len(arr2):
            if arr2[i] == '+':
                add = True
            elif arr2[i] == '-':
                sub = True
            else:
                if add:
                    res += arr2[i]
                    add = False
                elif sub:
                    res -= arr2[i]
                    sub = False
                else:
                    res = arr2[i]
            i += 1
        return res
