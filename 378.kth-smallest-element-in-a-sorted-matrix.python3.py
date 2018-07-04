#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (45.78%)
# Total Accepted:    65.5K
# Total Submissions: 143.1K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
#
#
# Example:
#
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
#
import heapq


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap, n = [], len(matrix)
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        i = 0
        while i < k-1:
            v, x, y = heapq.heappop(heap)
            if y+1 < n:
                heapq.heappush(heap, (matrix[x][y+1], x, y+1))
            i += 1
        return heapq.heappop(heap)[0]
