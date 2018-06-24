#
# [280] Wiggle Sort
#
# https://leetcode.com/problems/wiggle-sort/description/
#
# algorithms
# Medium (58.88%)
# Total Accepted:    44.8K
# Total Submissions: 76.2K
# Testcase Example:  '[3,5,2,1,6,4]'
#
# Given an unsorted array nums, reorder it in-place such that nums[0] <=
# nums[1] >= nums[2] <= nums[3]....
#
# Example:
#
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]
#


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i & 1 == 0:
                if nums[i+1] < nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i+1] > nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return
