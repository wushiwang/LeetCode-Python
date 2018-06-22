#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (53.70%)
# Total Accepted:    84.5K
# Total Submissions: 157.3K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
#
# Example:
#
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
#
# Note:
#
#
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
#


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        # Get a^b
        c = nums[0]
        for n in nums[1:]:
            c ^= n
        # Using lowbit() to split nums
        lb = c&-c
        a, b = None, None
        for n in nums:
            if n & lb == lb:
                a = n if a is None else a^n
            else:
                b = n if b is None else b^n
        return [a, b]
