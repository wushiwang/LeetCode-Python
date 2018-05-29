#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (23.32%)
# Total Accepted:    128.5K
# Total Submissions: 550.8K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max(self.cal(s), self.cal(self.rev(s)))

    def rev(self, s):
        tmp = list(s)
        for i in range(len(tmp)):
            if tmp[i] == '(':
                tmp[i] = ')'
            else:
                tmp[i] = '('
        return ''.join(tmp[::-1])

    def cal(self, s):
        lp, cur, res = 0, 0, 0
        for p in s:
            if p == ')':
                if lp != 0:
                    lp, cur = lp - 1, cur + 2
                    if lp == 0:
                        res = max(res, cur)
                else:
                    cur = 0
            else:
                lp = lp + 1
        return res
