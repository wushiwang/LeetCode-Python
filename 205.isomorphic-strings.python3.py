#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (34.99%)
# Total Accepted:    141.9K
# Total Submissions: 405.5K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.strToInt(s) == self.strToInt(t)

    def strToInt(self, s):
        res, cur = "", 0
        dic = dict()
        for c in s:
            if c not in dic:
                dic[c] = str(cur)
                cur += 1
            res += dic[c]
        return res
