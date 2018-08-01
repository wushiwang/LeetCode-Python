#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (37.85%)
# Total Accepted:    33.8K
# Total Submissions: 89.4K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
#
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
#
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
# Note:
#
# 1 k n
# Elements of the given array will be in the range [-10,000, 10,000].
#


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg = 0
        for i in range(k):
            avg += nums[i]
        avg /= k
        res = avg
        for i in range(k, len(nums)):
            s = avg*k - nums[i-k] + nums[i]
            avg = s / k
            res = max(res, avg)
        return res

