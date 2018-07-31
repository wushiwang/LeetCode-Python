#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.39%)
# Total Accepted:    28.1K
# Total Submissions: 86.6K
# Testcase Example:  '5'
#
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
#
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
#
#
# Example 2:
#
# Input: 3
# Output: False
#


class Solution:
    _dic = set()
    for i in range(46341):
        _dic.add(i**2)

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        dic = self._dic
        for v in dic:
            if v <= c and (c - v) in dic:
                return True
        return False
