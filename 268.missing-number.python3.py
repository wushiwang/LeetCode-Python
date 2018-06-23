#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (45.46%)
# Total Accepted:    182.4K
# Total Submissions: 401.2K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        L, R = 0, n
        while L < R:
            while L < R and nums[L] != L:
                if nums[L] >= n:
                    nums[L], nums[R-1] = nums[R-1], nums[L]
                    R -= 1
                else:
                    p = nums[L]
                    nums[L], nums[p] = nums[p], nums[L]
            if L != R:
                L += 1
        return nums[L-1]+1 if R != 0 else 0
