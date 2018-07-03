#
# [365] Water and Jug Problem
#
# https://leetcode.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (28.16%)
# Total Accepted:    21.1K
# Total Submissions: 74.7K
# Testcase Example:  '3\n5\n4'
#
# You are given two jugs with capacities x and y litres. There is an infinite
# amount of water supply available.
# You need to determine whether it is possible to measure exactly z litres
# using these two jugs.
#
# If z liters of water is measurable, you must have z liters of water contained
# within one or both buckets by the end.
#
#
# Operations allowed:
#
# Fill any of the jugs completely with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or
# the first jug itself is empty.
#
#
#
# Example 1: (From the famous "Die Hard" example)
#
# Input: x = 3, y = 5, z = 4
# Output: True
#
#
#
# Example 2:
#
# Input: x = 2, y = 6, z = 5
# Output: False
#
#
#
# Credits:Special thanks to @vinod23 for adding this problem and creating all
# test cases.
#


class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x+y:
            return False
        if z == x or z == y or z == x + y:
            return True

        return z % self._gcd(x, y) == 0

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)
