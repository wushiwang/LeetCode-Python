#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (47.08%)
# Total Accepted:    26.8K
# Total Submissions: 57K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
#
# Example 1:
#
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#
#
#
#
# Example 2:
#
# Input: [1,2,2,3,1,4,2]
# Output: 6
#
#
#
# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
#
import collections


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        degree = max([v for k, v in cnt.items()])
        cand = dict()
        for i in range(len(nums)):
            if cnt[nums[i]] == degree:
                if nums[i] not in cand:
                    cand[nums[i]] = [i, i]
                cand[nums[i]][1] = i
        return min([v[1]-v[0]+1 for k, v in cand.items()])