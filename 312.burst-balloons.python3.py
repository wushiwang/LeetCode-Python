#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (43.87%)
# Total Accepted:    41.1K
# Total Submissions: 93.8K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# Example:
#
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#


class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [[0 for x in range(len(nums))] for y in range(len(nums))]
        for i in range(0, len(nums)):
            for j in range(0, len(nums)-i):
                for k in range(j, j+i+1):
                    left = 0 if k == j else dp[j][k-1]
                    right = 0 if k == j+i else dp[k+1][j+i]
                    midl = 1 if j == 0 else nums[j-1]
                    midr = 1 if j+i == len(nums)-1 else nums[j+i+1]
                    dp[j][j+i] = max(dp[j][j+i], left+nums[k]*midl*midr+right)
        return dp[0][len(nums)-1]
