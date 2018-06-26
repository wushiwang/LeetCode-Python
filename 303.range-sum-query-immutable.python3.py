#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (32.94%)
# Total Accepted:    99.1K
# Total Submissions: 300.7K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n
# [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#
# Note:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
#


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.rec = []
        cur = 0
        for n in nums:
            cur += n
            self.rec.append(cur)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i != 0:
            return self.rec[j] - self.rec[i-1]
        else:
            return self.rec[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
