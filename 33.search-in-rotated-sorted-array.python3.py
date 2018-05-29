#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (31.94%)
# Total Accepted:    262.2K
# Total Submissions: 820.8K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        # get peak point, L, R -> []
        L, R = 0, len(nums) - 1
        while L < R - 1:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                L = M
            elif nums[M] < nums[L]:
                R = M
            else:
                L = M
        pv = L if nums[L] > nums[R] else R
        k = len(nums) - (pv + 1)

        # find target, [)
        L, R = 0, len(nums)
        while L < R:
            M = (L + R) // 2
            act = M - k if (M - k) >= 0 else M - k + len(nums)
            if nums[act] > target:
                R = M
            elif nums[act] < target:
                L = M + 1
            else:
                return act
        return -1
