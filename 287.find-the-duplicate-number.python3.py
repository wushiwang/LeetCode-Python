#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (44.89%)
# Total Accepted:    115.3K
# Total Submissions: 256.7K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
#
# Input: [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: [3,1,3,4,2]
# Output: 3
#
# Note:
#
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
#


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # (]
        L, R = 0, len(nums)-1
        while L < R-1:
            M = (L + R) >> 1
            cnt = self.count(nums, M)
            if cnt <= M:
                L = M
            else:
                R = M
        return R

    def count(self, nums, x):
        res = 0
        for n in nums:
            if n <= x:
                res += 1
        return res
