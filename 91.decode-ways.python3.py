#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (20.48%)
# Total Accepted:    175.9K
# Total Submissions: 859K
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
#


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s)+1):
            cur = int(s[i-2])*10 + int(s[i-1])
            if cur <= 26 and cur >= 10:
                dp[i] += dp[i-2]
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]

        return dp[len(s)]
