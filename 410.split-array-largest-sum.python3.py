#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (39.66%)
# Total Accepted:    25.3K
# Total Submissions: 63.7K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
#
#
# Note:
# If n is the length of array, assume the following constraints are satisfied:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
#
#
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#


class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # Binary Search
        L, R = max(nums)-1, sum(nums)+1
        while L < R-1:
            M = (L+R) >> 1
            if self.check(nums, M, m):
                R = M
            else:
                L = M
        return R

    def check(self, nums, target, m):
        s, cnt = 0, 1
        for i in range(len(nums)):
            s += nums[i]
            if s > target:
                cnt += 1
                s = nums[i]
        return cnt <= m
