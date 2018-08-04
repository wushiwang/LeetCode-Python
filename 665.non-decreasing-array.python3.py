#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.91%)
# Total Accepted:    30.1K
# Total Submissions: 151.2K
# Testcase Example:  '[4,2,3]'
#
#
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
#
#
#
# We define an array is non-decreasing if array[i]  holds for every i (1
#
# Example 1:
#
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
#
#
#
# Example 2:
#
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
#
#
#
# Note:
# The n belongs to [1, 10,000].
#
import math


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [-math.inf] + nums + [math.inf]
        modified = 0
        for i in range(1, len(nums)-2):
            if nums[i] > nums[i+1]:
                if nums[i+1] >= nums[i-1]:
                    nums[i] = nums[i+1]
                    modified += 1
                elif nums[i+1] < nums[i-1]:
                    modified += 1
                    nums[i+1] = nums[i+2]
                    if nums[i+1] < nums[i]:
                        return False
                else:
                    print(nums)
                    return False
        print(nums)
        return modified <= 1
