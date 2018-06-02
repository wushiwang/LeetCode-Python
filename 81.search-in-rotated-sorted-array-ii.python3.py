#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.62%)
# Total Accepted:    122.7K
# Total Submissions: 376.1K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true,
# otherwise return false.
#
# Example 1:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
#
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
#


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        # 1st
        L, R = 0, len(nums) - 1
        while L < R - 1:
            M = (L + R) // 2
            if nums[M] < nums[L]:
                R = M
            elif nums[M] > nums[L]:
                L = M
            else:
                L += 1
        if nums[L] > nums[R]:
            H = L + 1
        else:
            H = R + 1
        # 2nd
        L, R = 0, len(nums)
        while L < R:
            M = (L + R) // 2
            pos = (M+H) % len(nums)
            if nums[pos] > target:
                R = M
            elif nums[pos] < target:
                L = M + 1
            else:
                return True
        return False
