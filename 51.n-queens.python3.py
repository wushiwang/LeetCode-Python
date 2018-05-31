#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (33.70%)
# Total Accepted:    101.5K
# Total Submissions: 300.9K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# Example:
#
#
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
#


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.cc = [False for x in range(n)]
        self.cd1 = [False for x in range(2*n-1)]
        self.cd2 = [False for x in range(2*n-1)]
        self.cur = [['.' for x in range(n)] for y in range(n)]
        res = list()
        self.DFS(n, 0, res)
        return res

    def DFS(self, n, c, res):
        if c == n:
            res.append(list(map(lambda x: ''.join(x), self.cur)))
            return
        for i in range(n):
            if not (self.cc[i] or self.cd1[c-i+n-1] or self.cd2[i+c]):
                self.cc[i] = self.cd1[c-i+n-1] = self.cd2[i+c] = True
                self.cur[c][i] = 'Q'
                self.DFS(n, c+1, res)
                self.cur[c][i] = '.'
                self.cc[i] = self.cd1[c-i+n-1] = self.cd2[i+c] = False
