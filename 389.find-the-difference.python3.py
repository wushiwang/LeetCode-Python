#
# [389] Find the Difference
#
# https://leetcode.com/problems/find-the-difference/description/
#
# algorithms
# Easy (51.59%)
# Total Accepted:    111.2K
# Total Submissions: 215.5K
# Testcase Example:  '"abcd"\n"abcde"'
#
#
# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more
# letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.
#
import operator
import functools


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(functools.reduce(operator.xor, map(ord, s+t)))
