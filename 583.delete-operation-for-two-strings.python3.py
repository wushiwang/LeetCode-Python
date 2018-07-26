#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (44.77%)
# Total Accepted:    19.9K
# Total Submissions: 44.6K
# Testcase Example:  '"sea"\n"eat"'
#
#
# Given two words word1 and word2, find the minimum number of steps required to
# make word1 and word2 the same, where in each step you can delete one
# character in either string.
#
#
# Example 1:
#
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
#
#
#
# Note:
#
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
#


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        dp = [[0 for _ in  range(len(word2)+1)] for _ in range(len(word1)+1)]
        for j in range(1, len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[len(word1)][len(word2)]
