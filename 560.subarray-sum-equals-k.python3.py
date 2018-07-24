#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (39.81%)
# Total Accepted:    42K
# Total Submissions: 105.5K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
#
# Note:
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
#


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre, cur, res = dict(), 0, 0
        pre[0] = 1
        for i in range(len(nums)):
            cur += nums[i]
            if cur - k in pre:
                res += pre[cur-k]
            if cur not in pre:
                pre[cur] = 0
            pre[cur] += 1
        return res
