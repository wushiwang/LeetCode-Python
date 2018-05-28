#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (27.71%)
# Total Accepted:    159.6K
# Total Submissions: 575.8K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, nums = list(), sorted(nums)
        self.NSum(4, nums, target, list(), res)
        return res

    def NSum(self, n, nums, target, pre, res):
        """
        Transeform all N-Sum questions to 2-Sum questions
        N >= 2
        """
        if n < 2 or len(nums) < n:
            return

        if n == 2:
            L, R = 0, len(nums) - 1
            while L < R:
                cur = nums[L] + nums[R]
                if cur > target:
                    R = R - 1
                elif cur < target:
                    L = L + 1
                else:
                    res.append(pre+[nums[L], nums[R]])
                    L, R = L + 1, R - 1
                    while nums[L] == nums[L-1] and L < R:
                        L = L + 1
                    while nums[R] == nums[R+1] and L < R:
                        R = R - 1
        else:
            for i in range(0, len(nums)-n+1):
                if target < nums[i]*n or target > nums[-1]*n:
                    break
                if i == 0 or nums[i-1] != nums[i]:
                    self.NSum(n-1, nums[i+1:], target-nums[i],
                              pre+[nums[i]], res)
        return
