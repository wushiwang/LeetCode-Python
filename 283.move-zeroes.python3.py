#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (51.90%)
# Total Accepted:    306.3K
# Total Submissions: 590.1K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        fstZ = 0
        while fstZ < len(nums) and  nums[fstZ] != 0:
            fstZ += 1
        if fstZ == len(nums):
            return
        for i in range(len(nums)):
            if nums[i] != 0 and i > fstZ:
                nums[fstZ], nums[i] = nums[i], nums[fstZ]
                while fstZ < len(nums) and nums[fstZ] != 0:
                    fstZ += 1
                if fstZ == len(nums):
                    return
        return
