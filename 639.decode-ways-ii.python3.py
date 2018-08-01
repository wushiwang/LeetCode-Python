#
# [639] Decode Ways II
#
# https://leetcode.com/problems/decode-ways-ii/description/
#
# algorithms
# Hard (24.20%)
# Total Accepted:    14.4K
# Total Submissions: 59.4K
# Testcase Example:  '"*"'
#
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping way:
#
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#
# Beyond that, now the encoded string can also contain the character '*', which
# can be treated as one of the numbers from 1 to 9.
#
#
#
#
# Given the encoded message containing digits and the character '*', return the
# total number of ways to decode it.
#
#
#
# Also, since the answer may be very large, you should return the output mod
# 109 + 7.
#
#
# Example 1:
#
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C",
# "D", "E", "F", "G", "H", "I".
#
#
#
# Example 2:
#
# Input: "1*"
# Output: 9 + 9 = 18
#
#
#
# Note:
#
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.
#


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 1000000007
        if len(s) == 0:
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s)+1):
            if s[i-2] == '*' and s[i-1] == '*':
                dp[i] += 15*dp[i-2]
                dp[i] += 9*dp[i-1]
            elif s[i-2] == '*':
                cur = int(s[i-1])
                if cur >= 0 and cur <= 6:
                    dp[i] += 2*dp[i-2]
                else:
                    dp[i] += dp[i-2]
                if cur != 0:
                    dp[i] += dp[i-1]
            elif s[i-1] == '*':
                cur = int(s[i-2])
                if cur == 1:
                    dp[i] += 9*dp[i-2]
                elif cur == 2:
                    dp[i] += 6*dp[i-2]
                dp[i] += 9*dp[i-1]
            else:
                cur = int(s[i-2])*10 + int(s[i-1])
                if cur >= 10 and cur <= 26:
                    dp[i] += dp[i-2]
                if s[i-1] != '0':
                    dp[i] += dp[i-1]
            dp[i] %= MOD
        return dp[len(s)]
