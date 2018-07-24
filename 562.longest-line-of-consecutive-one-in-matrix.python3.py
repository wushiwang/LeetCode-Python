#
# [562] Longest Line of Consecutive One in Matrix
#
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/
#
# algorithms
# Medium (41.16%)
# Total Accepted:    8.2K
# Total Submissions: 19.9K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[0,0,0,1]]'
#
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# Example:
#
# Input:
# [[0,1,1,0],
#  ⁠[0,1,1,0],
#  ⁠[0,0,0,1]]
# Output: 3
#
#
#
#
# Hint:
# The number of elements in the given matrix will not exceed 10,000.
#


class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0:
            return 0
        res = 0

        for i in range(len(M)):
            cur = 1 if M[i][0] == 1 else 0
            res = max(res, cur)
            for j in range(1, len(M[0])):
                if M[i][j] == M[i][j-1] == 1:
                    cur += 1
                    res = max(res, cur)
                else:
                    res = max(res, cur)
                    cur = 1 if M[i][j] == 1 else 0

        for j in range(len(M[0])):
            cur = 1 if M[0][j] == 1 else 0
            res = max(res, cur)
            for i in range(1, len(M)):
                if M[i][j] == M[i-1][j] == 1:
                    cur += 1
                    res = max(res, cur)
                else:
                    res = max(res, cur)
                    cur = 1 if M[i][j] == 1 else 0

        for i in range(len(M)):
            x, y = i-1, 1
            cur = 1 if M[i][0] == 1 else 0
            res = max(res, cur)
            while x >= 0 and x < len(M) and y >= 0 and y < len(M[0]):
                if M[x][y] == M[x+1][y-1] == 1:
                    cur += 1
                    res = max(res, cur)
                else:
                    res = max(res, cur)
                    cur = 1 if M[x][y] == 1 else 0
                x, y = x-1, y+1

        for j in range(1, len(M[0])):
            x, y = len(M)-2, j+1
            cur = 1 if M[len(M)-1][j] == 1 else 0
            res = max(res, cur)
            while x >= 0 and x < len(M) and y >= 0 and y < len(M[0]):
                if M[x][y] == M[x+1][y-1] == 1:
                    cur += 1
                    res = max(res, cur)
                else:
                    res = max(res, cur)
                    cur = 1 if M[x][y] == 1 else 0
                x, y = x-1, y+1

        for i in range(len(M)):
            x, y = i+1, 1
            cur = 1 if M[i][0] == 1 else 0
            res = max(res, cur)
            while x >= 0 and x < len(M) and y >= 0 and y < len(M[0]):
                if M[x][y] == M[x-1][y-1] == 1:
                    cur += 1
                    res = max(res, cur)
                else:
                    res = max(res, cur)
                    cur = 1 if M[x][y] == 1 else 0
                x, y = x+1, y+1

        for j in range(1, len(M[0])):
            x, y = 1, j+1
            cur = 1 if M[0][j] == 1 else 0
            res = max(res, cur)
            while x >= 0 and x < len(M) and y >= 0 and y < len(M[0]):
                if M[x][y] == M[x-1][y-1] == 1:
                    cur += 1
                    res = max(res, cur)
                else:
                    res = max(res, cur)
                    cur = 1 if M[x][y] == 1 else 0
                x, y = x+1, y+1

        return res
