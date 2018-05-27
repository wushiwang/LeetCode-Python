#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (31.85%)
# Total Accepted:    178.6K
# Total Submissions: 560.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return
        nums, i = sorted(nums), 0
        res = nums[0] + nums[1] + nums[2]
        while i < len(nums):
            L, R, t = i+1, len(nums)-1, target-nums[i]
            while L < R:
                cur = nums[L] + nums[R]
                if abs(nums[i]+cur-target) < abs(res-target):
                    res = nums[i]+cur
                if cur > t:
                    R = R - 1
                    while nums[R] == nums[R+1] and L < R:
                        R = R - 1
                elif cur < t:
                    L = L + 1
                    while nums[L] == nums[L-1] and L < R:
                        L = L + 1
                else:
                    return target
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i = i + 1
            i = i + 1
        return res
