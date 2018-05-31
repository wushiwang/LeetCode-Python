#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (27.49%)
# Total Accepted:    147.1K
# Total Submissions: 534.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return list()
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        i, j, visited = 0, 0, {}
        visited[(0, 0)], res = True, [matrix[0][0]]
        while True:
            for x in range(4):
                while i+dx[x] != len(matrix) and i+dx[x] >= 0 and\
                        j+dy[x] != len(matrix[0]) and j+dy[x] >= 0 and\
                        (i+dx[x], j+dy[x]) not in visited:
                    i, j, res = i+dx[x], j+dy[x], res+[matrix[i+dx[x]][j+dy[x]]]
                    visited[(i, j)] = True
            if len(res) == len(matrix)*len(matrix[0]):
                break
        return res
