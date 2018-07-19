#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (43.20%)
# Total Accepted:    35.5K
# Total Submissions: 82.1K
# Testcase Example:  '"bbbab"'
#
#
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
#
#
# Example 1:
# Input:
#
# "bbbab"
#
# Output:
#
# 4
#
# One possible longest palindromic subsequence is "bbbb".
#
#
# Example 2:
# Input:
#
# "cbbd"
#
# Output:
#
# 2
#
# One possible longest palindromic subsequence is "bb".
#


class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s == s[::-1]:
            return len(s)
        dp = [[1]*2 for x in range(len(s))]
        for j in range(1, len(s)):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j&1] = dp[i+1][(j+1)&1] + 2 if i+1 <= j-1 else 2
                else:
                    dp[i][j&1] = max(dp[i+1][j&1], dp[i][(j+1)&1])
        return dp[0][(len(s)-1)&1]
