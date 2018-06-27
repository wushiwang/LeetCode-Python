#
# [308] Range Sum Query 2D - Mutable
#
# https://leetcode.com/problems/range-sum-query-2d-mutable/description/
#
# algorithms
# Hard (26.74%)
# Total Accepted:    24K
# Total Submissions: 89.6K
# Testcase Example:  '["NumMatrix","sumRegion","update","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[3,2,2],[2,1,4,3]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
#
#
#
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
#
#
# Example:
#
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
#
#
#
# Note:
#
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is
# distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
#


class NumMatrix:

    class BIT2D:
        def __init__(self, matrix):
            if len(matrix) == 0:
                return
            self.bit = [[0]*(len(matrix[0])+1) for y in range(len(matrix)+1)]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    self.update(i, j, matrix[i][j])

        def update(self, x, y, v):
            i = x+1
            while i < len(self.bit):
                j = y+1
                while j < len(self.bit[0]):
                    self.bit[i][j] += v
                    j += j & (-j)
                i += i & (-i)

        def sum(self, x, y):
            i, res = x+1, 0
            while i > 0:
                j = y+1
                while j > 0:
                    res += self.bit[i][j]
                    j -= j & (-j)
                i -= i & (-i)
            return res

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.bit = self.BIT2D(matrix)
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.bit.update(row, col, val-self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 != 0 and col1 != 0:
            return self.bit.sum(row2, col2) - self.bit.sum(row1-1, col2) - self.bit.sum(row2, col1-1) +\
                self.bit.sum(row1-1, col1-1)
        elif row1 != 0:
            return self.bit.sum(row2, col2) - self.bit.sum(row1-1, col2)
        elif col1 != 0:
            return self.bit.sum(row2, col2) - self.bit.sum(row2, col1-1)
        else:
            return self.bit.sum(row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
