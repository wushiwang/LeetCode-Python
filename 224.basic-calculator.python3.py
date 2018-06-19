#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (29.08%)
# Total Accepted:    69.1K
# Total Submissions: 237.6K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
#
# Example 1:
#
#
# Input: "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: " 2-1 + 2 "
# Output: 3
#
# Example 3:
#
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
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
        res, i = self.helper(s, 0)
        return res

    def helper(self, s, pos):
        res, i, add, sub = 0, pos, False, False
        while i < len(s) and s[i] != ')':
            if s[i] != ' ':
                if s[i] == '(':
                    num, i = self.helper(s, i+1)
                    if add:
                        res += num
                        add = False
                    elif sub:
                        res -= num
                        sub = False
                    else:
                        res = num
                elif s[i] == '+':
                    add = True
                elif s[i] == '-':
                    sub = True
                else:
                    num = int(s[i])
                    while i+1 < len(s) and ord(s[i+1]) >= ord('0') and ord(s[i+1]) <= ord('9'):
                        i += 1
                        num *= 10
                        num += int(s[i])
                    if add:
                        res += num
                        add = False
                    elif sub:
                        res -= num
                        sub = False
                    else:
                        res = num
            i += 1
        return res, i
