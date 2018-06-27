#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (23.20%)
# Total Accepted:    47K
# Total Submissions: 202.6K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n
# [[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i
# to val.
#
# Example:
#
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
# Note:
#
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
#


class NumArray:

    class BIT:
        def __init__(self, nums):
            self.bit = [0]*(len(nums)+1)
            for i in range(len(nums)):
                self.update(i, nums[i])

        def update(self, i, v):
            i += 1
            while i < len(self.bit):
                self.bit[i] += v
                i += i & (-i)

        def sum(self, i):
            i, res = i+1, 0
            while i != 0:
                res += self.bit[i]
                i -= i & (-i)
            return res

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.bit = self.BIT(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.bit.update(i, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.bit.sum(j)
        else:
            return self.bit.sum(j) - self.bit.sum(i-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
