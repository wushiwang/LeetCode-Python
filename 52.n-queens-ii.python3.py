#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (47.20%)
# Total Accepted:    76.6K
# Total Submissions: 162.2K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
#
# Example:
#
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
#
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
#


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cc = [False for x in range(n)]
        self.cd1 = [False for x in range(2*n-1)]
        self.cd2 = [False for x in range(2*n-1)]
        self.res = 0
        self.DFS(n, 0)
        return self.res

    def DFS(self, n, c):
        if c == n:
            self.res += 1
            return
        for i in range(n):
            if not (self.cc[i] or self.cd1[c-i+n-1] or self.cd2[i+c]):
                self.cc[i] = self.cd1[c-i+n-1] = self.cd2[i+c] = True
                self.DFS(n, c+1)
                self.cc[i] = self.cd1[c-i+n-1] = self.cd2[i+c] = False
