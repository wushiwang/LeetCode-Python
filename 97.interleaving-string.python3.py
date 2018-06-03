#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (25.41%)
# Total Accepted:    85.3K
# Total Submissions: 335.6K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        dp = [[False for x in range(len(s1)+1)] for y in range(len(s2)+1)]
        for i in range(1, len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[0][i] = True
            else:
                break
        for j in range(1, len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[j][0] = True
            else:
                break
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if dp[i-1][j] and s3[i+j-1] == s2[i-1]:
                    dp[i][j] = True
                elif dp[i][j-1] and s3[i+j-1] == s1[j-1]:
                    dp[i][j] = True
        return dp[len(s2)][len(s1)]
