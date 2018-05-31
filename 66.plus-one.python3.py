#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.84%)
# Total Accepted:    250.1K
# Total Submissions: 627.7K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        res, add = list(), 0
        digits[-1] += 1
        for d in digits[::-1]:
            d, add = d+add, 0
            if d >= 10:
                d, add = d-10, 1
            res = [d] + res
        if add == 1:
            res = [1] + res
        return res
