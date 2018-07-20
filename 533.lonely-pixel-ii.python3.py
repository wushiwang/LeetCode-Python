#
# [533] Lonely Pixel II
#
# https://leetcode.com/problems/lonely-pixel-ii/description/
#
# algorithms
# Medium (45.39%)
# Total Accepted:    6.7K
# Total Submissions: 14.8K
# Testcase Example:  '[["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]]\n3'
#
# Given a picture consisting of black and white pixels, and a positive integer
# N, find the number of black pixels located at some specific row R and column
# C that align with all the following rules:
#
#
# ⁠Row R and column C both contain exactly N black pixels.
# ⁠For all rows that have a black pixel at column C, they should be exactly the
# same as row R
#
#
# The picture is represented by a 2D char array consisting of 'B' and 'W',
# which means black and white pixels respectively.
#
# Example:
#
# Input:
# [['W', 'B', 'W', 'B', 'B', 'W'],
# ⁠['W', 'B', 'W', 'B', 'B', 'W'],
# ⁠['W', 'B', 'W', 'B', 'B', 'W'],
# ⁠['W', 'W', 'B', 'W', 'B', 'W']]
#
# N = 3
# Output: 6
# Explanation: All the bold 'B' are the black pixels we need (all 'B's at
# column 1 and 3).
# ⁠       0    1    2    3    4    5         column
# index
# 0    [['W', 'B', 'W', 'B', 'B', 'W'],
# 1     ['W', 'B', 'W', 'B', 'B', 'W'],
# 2     ['W', 'B', 'W', 'B', 'B', 'W'],
# 3     ['W', 'W', 'B', 'W', 'B', 'W']]
# row index
#
#
#
#
# Note:
#
# The range of width and height of the input 2D array is [1,200].
#


class Solution:
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        row = [0]*(len(picture))
        col = [0]*(len(picture[0]))
        for i in range(len(picture)):
            cur = 0
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    cur += 1
            row[i] = cur
        for j in range(len(picture[0])):
            cur = 0
            for i in range(len(picture)):
                if picture[i][j] == 'B':
                    cur += 1
            col[j] = cur
        dic, pos = dict(), 0
        rec = [0]*(len(picture))
        for i in range(len(picture)):
            cur = tuple(picture[i])
            if cur not in dic:
                dic[cur] = pos
                pos += 1
            rec[i] = dic[cur]
        ext = [False]*len(picture[0])
        for j in range(len(picture[0])):
            tmp = []
            for i in range(len(picture)):
                if picture[i][j] == 'B':
                    tmp.append(rec[i])
            if len(set(tmp)) == 1:
                ext[j] = True
        res = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and row[i] == col[j] == N and ext[j]:
                    res += 1
        return res
