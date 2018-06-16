#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (32.49%)
# Total Accepted:    122.6K
# Total Submissions: 377.1K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
#
# Example: 
#
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
#
import math


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        L, R, cur = 0, 0, 0
        res = math.inf
        while R < len(nums):
            cur += nums[R]
            while cur >= s:
                res = min(res, R-L+1)
                cur -= nums[L]
                L += 1
            R += 1
        return res if res != math.inf else 0

