#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (46.87%)
# Total Accepted:    22.1K
# Total Submissions: 47.2K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
#
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
#
#
#
# Note:
#
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
#
import math


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        dx = [1, 0, 0, -1, 1, 1, -1, -1]
        dy = [0, 1, -1, 0, 1, -1, 1, -1]
        if len(M) == 0:
            return M
        res = [[0]*len(M[0]) for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                cur, cnt = M[i][j], 1
                for d in range(8):
                    nx, ny = i+dx[d], j+dy[d]
                    if nx >= 0 and nx < len(M) and ny >= 0 and ny < len(M[0]):
                        cur += M[nx][ny]
                        cnt += 1
                res[i][j] = math.floor(cur/cnt)
        return res
