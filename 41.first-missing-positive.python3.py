#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (26.04%)
# Total Accepted:    136.7K
# Total Submissions: 524.6K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        if nums[0] != 1:
            return 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                return i+1
        return len(nums)+1
