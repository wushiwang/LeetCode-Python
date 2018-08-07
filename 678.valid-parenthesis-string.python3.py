#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (29.71%)
# Total Accepted:    13.5K
# Total Submissions: 45.4K
# Testcase Example:  '"()"'
#
#
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#


class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.dic = dict()
        return self.DFS(s, 0, 0)

    def DFS(self, s, pos, n):
        if pos == len(s):
            return True if n == 0 else False
        if (pos, n) in self.dic:
            return self.dic[(pos, n)]
        if n < 0:
            return False
        if s[pos] == '(':
            res = self.DFS(s, pos+1, n+1)
        elif s[pos] == ')':
            res = self.DFS(s, pos+1, n-1)
        else:
            res = self.DFS(s, pos+1, n) or self.DFS(s, pos+1, n+1) or self.DFS(s, pos+1, n-1)
        self.dic[(pos, n)] = res
        return res
