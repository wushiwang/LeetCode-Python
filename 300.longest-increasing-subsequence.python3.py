#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (39.03%)
# Total Accepted:    134.1K
# Total Submissions: 343.6K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
# Note:
#
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp, res = [0 for x in nums], 1
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j], dp[i])
            dp[i] += 1
            res = max(res, dp[i])
        return res
