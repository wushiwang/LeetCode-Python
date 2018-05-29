#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range/description/
#
# algorithms
# Medium (31.69%)
# Total Accepted:    194.8K
# Total Submissions: 614.6K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        # first BS, [)
        res1, res2 = -1, -1
        L, R = -1, len(nums) - 1
        while L < R - 1:
            M = (L + R) // 2
            if nums[M] >= target:
                R = M
            else:
                L = M
        res1 = R if nums[R] == target else -1
        # second BS, (]
        L, R = 0, len(nums)
        while L < R - 1:
            M = (L + R) // 2
            if nums[M] > target:
                R = M
            else:
                L = M
        res2 = L if nums[L] == target else -1

        return [res1, res2]
