#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.43%)
# Total Accepted:    322.4K
# Total Submissions: 1.3M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str rtype: str
        """
        if len(s) == 0:
            return ""
        res, res_str = 1, s[0]
        for i, c in enumerate(s):
            L, R, cur_len = i - 1, i + 1, 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L, R, cur_len = L - 1, R + 1, cur_len + 2
            if cur_len > res:
                res, res_str = cur_len, s[L + 1:R]
            L, R, cur_len = i, i + 1, 0
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L, R, cur_len = L - 1, R + 1, cur_len + 2
            if cur_len > res:
                res, res_str = cur_len, s[L + 1:R]
        return res_str
