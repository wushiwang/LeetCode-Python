#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (48.52%)
# Total Accepted:    214.9K
# Total Submissions: 442.8K
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list()
        self.DFS(n, n, res, "")
        return res

    def DFS(self, L, R, res, cur):
        if L == 0 and R == 0:
            res.append(cur)
            return
        if L != 0:
            self.DFS(L-1, R, res, cur + '(')
        if R != 0 and R > L:
            self.DFS(L, R-1, res, cur + ')')
        return
