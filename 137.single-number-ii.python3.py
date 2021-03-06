#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (42.95%)
# Total Accepted:    137.1K
# Total Submissions: 318.9K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            s = 0
            for n in nums:
                s += (n >> i) & 1
            res |= (s % 3) << i
        return res if res <= 2**31-1 else res-2**32
