#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (33.93%)
# Total Accepted:    35.9K
# Total Submissions: 106K
# Testcase Example:  '[1,2,3]'
#
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj %
# Si = 0.
#
#
# If there are multiple solutions, return any subset is fine.
#
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]
#
#
#
# Credits:Special thanks to @Stomach_ache for adding this problem and creating
# all test cases.
#


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        dp = [(1, i, i) for i in range(len(nums))]
        maxx = (1, 0, 0)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if dp[j][0]+1 > dp[i][0]:
                        dp[i] = (dp[j][0]+1, i, j)
                    if dp[i][0] > maxx[0]:
                        maxx = dp[i]
        res = []
        while maxx[1] != maxx[2]:
            res.append(nums[maxx[1]])
            maxx = dp[maxx[2]]
        res.append(nums[maxx[1]])
        return res
