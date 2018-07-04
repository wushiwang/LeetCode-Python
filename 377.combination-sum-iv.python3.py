#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (42.99%)
# Total Accepted:    63K
# Total Submissions: 146.6K
# Testcase Example:  '[1,2,3]\n4'
#
# ⁠Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
#
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
#
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#


class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = set(list(filter(lambda x: x <= target, nums)))
        dp = [0 for x in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for j in nums:
                if j <= i:
                    dp[i] += dp[i-j]
        return dp[target]
