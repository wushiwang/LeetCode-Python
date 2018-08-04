#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (31.99%)
# Total Accepted:    19K
# Total Submissions: 59.4K
# Testcase Example:  '[1,3,5,4,7]'
#
#
# Given an unsorted array of integers, find the number of longest increasing
# subsequence.
#
#
# Example 1:
#
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1,
# 3, 5, 7].
#
#
#
# Example 2:
#
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
#
#
#
# Note:
# Length of the given array will be not exceed 2000 and the answer is
# guaranteed to be fit in 32-bit signed int.
#


class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        l = [1]*(len(nums))
        v = [1]*(len(nums))
        lis = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if l[j]+1 > l[i]:
                        l[i], v[i] = l[j] + 1, 0
            for j in range(i):
                if nums[i] > nums[j] and l[i] == l[j]+1:
                    v[i] += v[j]
            lis = max(lis, l[i])
        res = 0
        for i in range(len(nums)):
            if l[i] == lis:
                res += v[i]
        return res
