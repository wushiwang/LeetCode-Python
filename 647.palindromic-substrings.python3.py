#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (54.41%)
# Total Accepted:    51K
# Total Submissions: 93.7K
# Testcase Example:  '"abc"'
#
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
#
#
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Note:
#
# The input string length won't exceed 1000.
#


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False]*len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        for l in range(2, len(s)+1):
            for i in range(len(s)-l+1):
                if l == 2:
                    dp[i][i+1] = (s[i] == s[i+1])
                else:
                    dp[i][i+l-1] = (s[i] == s[i+l-1]) and (dp[i+1][i+l-2])
                if dp[i][i+l-1]:
                    res += 1
        return res
