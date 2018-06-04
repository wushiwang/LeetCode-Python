#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (32.30%)
# Total Accepted:    84.4K
# Total Submissions: 261.2K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# Example 2:
#
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
#
#
#
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(t) == 0:
            return 1
        dp = [[0 for x in range(len(s))] for y in range(2)]
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, len(s)):
            dp[0][i] = dp[0][i-1] + 1 if s[i] == t[0] else dp[0][i-1]
        for i in range(1, len(t)):
            dp[i&1][i-1] = 0
            for j in range(i, len(s)):
                dp[i&1][j] = dp[i&1][j-1]+dp[(i+1)&1][j-1] if t[i] == s[j] else dp[i&1][j-1]

        return dp[(len(t)-1)&1][len(s)-1]
