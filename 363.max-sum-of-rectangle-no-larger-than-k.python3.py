#
# [363] Max Sum of Rectangle No Larger Than K
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (33.93%)
# Total Accepted:    20.5K
# Total Submissions: 60.4K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a
# rectangle in the matrix such that its sum is no larger than k.
#
# Example:
# Given matrix = [
# ⁠ [1,  0, 1],
# ⁠ [0, -2, 3]
# ]
# k = 2
#
#
#
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is
# the max number no larger than k (k = 2).
#
# Note:
#
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?
#
#
#
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all
# test cases.
#
import bisect
import math


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Transform 2-D problem to 1-D problem
        # For example:
        # 1  0 1
        # 0 -2 3
        # when we need to use row 0 and row1, we can just add them to 1-D
        # array: 1 -2 4 and solve it.
        if len(matrix[0]) < len(matrix):
            matrix[:] = zip(*matrix[::-1])
        res = -math.inf
        for i in range(len(matrix)):
            cur = [0]*len(matrix[0])
            for j in range(i, len(matrix)):
                for x in range(len(matrix[0])):
                    cur[x] += matrix[j][x]
                res = max(res, self.maxSum1D(cur, k))
        return res

    def maxSum1D(self, nums, k):
        # The expected time complexity should be O(nlgn)
        # However, python does not have build-in Balanced BST
        # We use binary search and list instead
        pre, cur, res = [0], 0, -math.inf
        for n in nums:
            cur += n
            # Lower bound
            pos = bisect.bisect_left(pre, cur-k)
            if pos >= 0 and pos < len(pre):
                res = max(res, cur-pre[pos])
            bisect.insort(pre, cur)
        return res
