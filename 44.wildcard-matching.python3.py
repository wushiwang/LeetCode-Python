#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (21.13%)
# Total Accepted:    126.5K
# Total Submissions: 598.3K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
#
#
# Example 4:
#
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
#
#
# Example 5:
#
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
#


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for x in range(len(p)+1)] for y in range(2)]
        for i in range(len(s)+1):
            if i == 0:
                dp[i&1][0] = True
            else:
                dp[i&1][0] = False
            for j in range(1, len(p)+1):
                dp[i&1][j] = False
                if p[j-1] == '*':
                    dp[i&1][j] = dp[i&1][j-1] or dp[(i+1)&1][j-1] or dp[(i+1)&1][j]
                elif p[j-1] == '?' or (i > 0 and s[i-1] == p[j-1]):
                    dp[i&1][j] = dp[(i+1)&1][j-1] if i > 0 else False
        return dp[len(s)&1][len(p)]
