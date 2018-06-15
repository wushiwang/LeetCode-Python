#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (23.74%)
# Total Accepted:    96.4K
# Total Submissions: 406K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
#
# Example 1:
#
#
# Input: [10,2]
# Output: "210"
#
# Example 2:
#
#
# Input: [3,30,34,5,9]
# Output: "9534330"
#
#
# Note: The result may be very large, so you need to return a string instead of
# an integer.
#
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return ''.join(sorted(map(str, nums), key=cmp_to_key(lambda x, y: (x+y>y+x)-(x+y<y+x)), reverse=True)).lstrip('0') or '0'
