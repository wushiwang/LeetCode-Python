#
# [259] 3Sum Smaller
#
# https://leetcode.com/problems/3sum-smaller/description/
#
# algorithms
# Medium (42.28%)
# Total Accepted:    37.6K
# Total Submissions: 88.9K
# Testcase Example:  '[-2,0,1,3]\n2'
#
# Given an array of n integers nums and a target, find the number of index
# triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] +
# nums[j] + nums[k] < target.
#
# Example:
#
#
# Input: nums = [-2,0,1,3], and target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than
# 2:
# [-2,0,1]
# ⁠            [-2,0,3]
#
#
# Follow up: Could you solve it in O(n2) runtime?
#


class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 2:
            return 0
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)-2):
            cur = target - nums[i]
            L, R = i+1, len(nums)-1
            while L != R:
                if nums[L] + nums[R] >= cur:
                    R -= 1
                else:
                    res += R - L
                    L += 1
        return res
