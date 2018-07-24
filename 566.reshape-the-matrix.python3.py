#
# [566] Reshape the Matrix
#
# https://leetcode.com/problems/reshape-the-matrix/description/
#
# algorithms
# Easy (57.71%)
# Total Accepted:    55.5K
# Total Submissions: 96.2K
# Testcase Example:  '[[1,2],[3,4]]\n1\n4'
#
# In MATLAB, there is a very useful function called 'reshape', which can
# reshape a matrix into a new one with different size but keep its original
# data.
#
#
#
# You're given a matrix represented by a two-dimensional array, and two
# positive integers r and c representing the row number and column number of
# the wanted reshaped matrix, respectively.
#
# ⁠The reshaped matrix need to be filled with all the elements of the original
# matrix in the same row-traversing order as they were.
#
#
#
# If the 'reshape' operation with given parameters is possible and legal,
# output the new reshaped matrix; Otherwise, output the original matrix.
#
#
# Example 1:
#
# Input:
# nums =
# [[1,2],
# ⁠[3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]
# Explanation:The row-traversing of nums is [1,2,3,4]. The new reshaped matrix
# is a 1 * 4 matrix, fill it row by row by using the previous list.
#
#
#
# Example 2:
#
# Input:
# nums =
# [[1,2],
# ⁠[3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
# ⁠[3,4]]
# Explanation:There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So
# output the original matrix.
#
#
#
# Note:
#
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.
#


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return nums
        if r*c != len(nums)*len(nums[0]):
            return nums
        self.vector(nums)
        res, pos = [[] for _ in range(r)], 0
        for i in range(r):
            for j in range(c):
                res[i].append(self.tmp[pos])
                pos += 1
        return res

    def vector(self, nums):
        self.tmp = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                self.tmp.append(nums[i][j])
