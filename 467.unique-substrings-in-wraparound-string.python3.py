#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
#
# algorithms
# Medium (33.39%)
# Total Accepted:    13.6K
# Total Submissions: 40.8K
# Testcase Example:  '"a"'
#
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
#
# Now we have another string p. Your job is to find out how many unique
# non-empty substrings of p are present in s. In particular, your input is the
# string p and you need to output the number of different non-empty substrings
# of p in the string s.
#
# Note: p consists of only lowercase English letters and the size of p might be
# over 10000.
#
# Example 1:
#
# Input: "a"
# Output: 1
#
# Explanation: Only the substring "a" of string "a" is in the string s.
#
#
#
# Example 2:
#
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string
# s.
#
#
#
# Example 3:
#
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
# string "zab" in the string s.
#


class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if len(p) == 0:
            return 0

        def ctoi(c):
            return ord(c) - ord('a')

        dp, cur = [0 for x in range(26)], 1
        dp[ctoi(p[0])] = 1
        for i in range(1, len(p)):
            if ctoi(p[i]) == (ctoi(p[i-1]) + 1) % 26:
                cur += 1
            else:
                cur = 1
            dp[ctoi(p[i])] = max(dp[ctoi(p[i])], cur)
        return sum(dp)
