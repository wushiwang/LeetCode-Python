#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.61%)
# Total Accepted:    161.5K
# Total Submissions: 466.7K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        if n == 0:
            return False
        if target < matrix[0][0]:
            return False
        # First binary search, get row number
        L, R = 0, m
        while L < R - 1:
            M = (L + R) // 2
            if matrix[M][0] <= target:
                L = M
            else:
                R = M
        r = L
        if matrix[r][0] == target:
            return True
        # Second binary search, get colomn number
        L, R = 0, n
        while L < R:
            M = (L + R) // 2
            if matrix[r][M] < target:
                L = M + 1
            elif matrix[r][M] > target:
                R = M
            else:
                return True
        return False
