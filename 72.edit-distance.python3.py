#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (32.89%)
# Total Accepted:    119.2K
# Total Submissions: 361.7K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for x in range(n+1)] for y in range(2)]
        for i in range(n+1):
            dp[0][i] = i
        for i in range(1, m+1):
            dp[i&1][0] = i
            a, b = i&1, (i+1)&1
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[a][j] = dp[b][j-1]
                else:
                    if i > 0 and j > 0:
                        dp[a][j] = min(dp[b][j], dp[a][j-1], dp[b][j-1]) + 1
        return dp[m&1][n]

