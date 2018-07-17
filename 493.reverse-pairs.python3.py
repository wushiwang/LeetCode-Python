#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (20.73%)
# Total Accepted:    13.2K
# Total Submissions: 63.8K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and
# nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
#
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
#
# Note:
#
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
#
import math
import bisect


class Solution:
    class BIT:
        def __init__(self, n):
            self.bit = [0]*(n+1)

        def update(self, x, v):
            x += 1
            while x < len(self.bit):
                self.bit[x] += v
                x += x & (-x)

        def sum(self, x):
            x, res = x+1, 0
            while x > 0:
                res += self.bit[x]
                x -= x & (-x)
            return res

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nn = sorted(list(set(nums)))
        dic = dict()
        for i in range(len(nn)):
            dic[nn[i]] = i
        bit, res = self.BIT(len(nn)), 0
        for i in range(len(nums)-1, -1, -1):
            pos = bisect.bisect_left(nn, math.ceil(nums[i]/2))
            if pos != 0:
                res += bit.sum(dic[nn[pos-1]])
            bit.update(dic[nums[i]], 1)
        return res
