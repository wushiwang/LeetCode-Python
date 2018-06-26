#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (36.01%)
# Total Accepted:    73K
# Total Submissions: 202.6K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and
# ).
#
# Example 1:
#
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
#
#
# Example 2:
#
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#
#
# Example 3:
#
#
# Input: ")("
# Output: [""]
#


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return [""]
        res = set()
        self.le = 0
        if s[0] == ')':
            self.DFS(s[1:], 0, 0, res, "")
        else:
            self.DFS(s, 0, 0, res, "")
        return list(res)

    def DFS(self, s, l, r, res, cur):
        if s == '':
            if l == r:
                if len(cur) < self.le:
                    return
                elif len(cur) > self.le:
                    res.clear()
                res.add(cur)
                self.le = len(cur)
            return
        # Pruning
        if len(cur) + len(s) < self.le:
            return
        nl, nr = l, r
        if s[0] == '(':
            nl += 1
        elif s[0] == ')':
            nr += 1
        else:
            self.DFS(s[1:], l, r, res, cur+s[0])
            return
        if r <= l:
            self.DFS(s[1:], nl, nr, res, cur+s[0])
            self.DFS(s[1:], l, r, res, cur)

