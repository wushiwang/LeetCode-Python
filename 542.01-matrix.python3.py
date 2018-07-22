#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (33.18%)
# Total Accepted:    23.8K
# Total Submissions: 71.8K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
import math
import collections


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dx = [0,1,-1,0]
        dy = [1,0,0,-1]
        que = collections.deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = math.inf
                else:
                    que.append((i, j, 0))
        while len(que) != 0:
            x, y, v = que.popleft()
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if nx >= 0 and nx < len(matrix) and\
                        ny >= 0 and ny < len(matrix[0]) and\
                        matrix[nx][ny] > v+1:
                    matrix[nx][ny] = v+1
                    que.append((nx, ny, v+1))
        return matrix
