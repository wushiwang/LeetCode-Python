#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (39.05%)
# Total Accepted:    20.1K
# Total Submissions: 51.4K
# Testcase Example:  '[4,6,7,7]'
#
#
# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2 .
#
#
# Example:
#
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
#
#
#
# Note:
#
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.
#


class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, i = set(), 0
        while i < len(nums):
            self.DFS(i+1, nums, res, [nums[i]])
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return list(res)

    def DFS(self, pos, nums, res, cur):
        i = pos
        while i < len(nums):
            if nums[i] >= cur[-1]:
                res.add(tuple(cur+[nums[i]]))
                self.DFS(i+1, nums, res, cur+[nums[i]])
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
