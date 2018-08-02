#
# [644] Maximum Average Subarray II
#
# https://leetcode.com/problems/maximum-average-subarray-ii/description/
#
# algorithms
# Hard (25.74%)
# Total Accepted:    6K
# Total Submissions: 23.2K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
#
# Given an array consisting of n integers, find the contiguous subarray whose
# length is greater than or equal to k that has the maximum average value. And
# you need to output the maximum average value.
#
#
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
#
#
#
#
# Note:
#
# 1 k n
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10-5 will be accepted.
#


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        EPS = 1e-5
        L, R = min(nums), max(nums)
        while (R - L) > EPS:
            M = (L + R) / 2.0
            if self.check(M, nums, k):
                L = M
            else:
                R = M
        return R

    def check(self, v, nums, k):
        cur = 0
        for i in range(k-1):
            cur += nums[i] - v
        minPre, pre = 0, 0
        for i in range(k-1, len(nums)):
            cur += nums[i] - v
            if cur - minPre > 0:
                return True
            pre += nums[i-k+1] - v
            minPre = min(minPre, pre)
        return False
