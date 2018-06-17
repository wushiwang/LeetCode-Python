#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (34.69%)
# Total Accepted:    80.2K
# Total Submissions: 231.1K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for n in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        res_l = max(dp[0], dp[1])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            res_l = max(res_l, dp[i])
        nums = nums[::-1]
        dp = [0 for n in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        res_r = max(dp[0], dp[1])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            res_r = max(res_r, dp[i])
        return max(res_l, res_r)
