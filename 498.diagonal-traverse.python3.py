#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (44.75%)
# Total Accepted:    22.7K
# Total Submissions: 50.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
#
#
# Example:
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
#
#
#
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.
#


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        dx = [-1,1]
        dy = [1,-1]
        res, direction, x, y = [], True, 0, 0
        while len(res) != len(matrix)*len(matrix[0]):
            if direction:
                nx, ny = x, y
                while True:
                    res.append(matrix[nx][ny])
                    if not (nx+dx[0] >= 0 and nx+dx[0] < len(matrix) and\
                            ny+dy[0] >= 0 and ny+dy[0] < len(matrix[0])):
                        break
                    else:
                        nx, ny = nx+dx[0], ny+dy[0]
                if ny == len(matrix[0])-1:
                    x, y, direction = nx+1, ny, False
                else:
                    x, y, direction = nx, ny+1, False
            else:
                nx, ny = x, y
                while True:
                    res.append(matrix[nx][ny])
                    if not (nx+dx[1] >= 0 and nx+dx[1] < len(matrix) and\
                            ny+dy[1] >= 0 and ny+dy[1] < len(matrix[0])):
                        break
                    else:
                        nx, ny = nx+dx[1], ny+dy[1]
                if nx == len(matrix) -1:
                    x, y, direction = nx, ny+1, True
                else:
                    x, y, direction = nx+1, ny, True
        return res
