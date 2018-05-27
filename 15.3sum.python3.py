#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (21.80%)
# Total Accepted:    330.2K
# Total Submissions: 1.5M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, res, i = sorted(nums), [], 0
        while i < len(nums):
            L, R, target = i+1, len(nums) - 1, -1 * nums[i]
            while L < R:
                cur = nums[L] + nums[R]
                if cur > target:
                    R = R - 1
                    while nums[R] == nums[R + 1] and L < R:
                        R = R - 1
                elif cur < target:
                    L = L + 1
                    while nums[L] == nums[L - 1] and L < R:
                        L = L + 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L, R = L + 1, R - 1
                    while nums[R] == nums[R + 1] and\
                            nums[L] == nums[L - 1] and L < R:
                        L, R = L + 1, R - 1
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i = i + 1
            i = i + 1
        return res
