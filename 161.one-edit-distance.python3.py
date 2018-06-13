#
# [161] One Edit Distance
#
# https://leetcode.com/problems/one-edit-distance/description/
#
# algorithms
# Medium (31.54%)
# Total Accepted:    52.9K
# Total Submissions: 167.9K
# Testcase Example:  '"ab"\n"acb"'
#
# Given two strings s and t, determine if they are both one edit distance
# apart.
#
# Note: 
#
# There are 3 possiblities to satisify one edit distance apart:
#
#
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
#
#
# Example 1:
#
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
#
#
# Example 2:
#
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
#
# Example 3:
#
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.
#


class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if abs(m-n) > 1:
            return False
        if m == n:
            change = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    change += 1
            return change == 1
        else:
            if m < n:
                m, n, s, t = n, m, t, s
            for i in range(len(s)):
                if s[:i]+s[i+1:] == t:
                    return True
            return False
