#
# [319] Bulb Switcher
#
# https://leetcode.com/problems/bulb-switcher/description/
#
# algorithms
# Medium (43.06%)
# Total Accepted:    49.5K
# Total Submissions: 115K
# Testcase Example:  '3'
#
# There are n bulbs that are initially off. You first turn on all the bulbs.
# Then, you turn off every second bulb. On the third round, you toggle every
# third bulb (turning on if it's off or turning off if it's on). For the i-th
# round, you toggle every i bulb. For the n-th round, you only toggle the last
# bulb. Find how many bulbs are on after n rounds.
#
# Example:
#
#
# Input: 3
# Output: 1
# Explanation:
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off].
#
# So you should return 1, because there is only one bulb is on.
#
# n = 3
# o o o
# x x x
# x o x
# x o o
#
# n = 4
# o o o o
# x x x x
# x o x o
# x o o x
# x o o x
#
# n = 5
# o o o o o
# x x x x x 1
# x o x o x 2
# x o o o x 3
# x o o x x 4
# x o o x o 5
#
import math


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.floor(math.sqrt(n))
