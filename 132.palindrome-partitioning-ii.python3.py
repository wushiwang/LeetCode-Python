#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (25.06%)
# Total Accepted:    83.1K
# Total Submissions: 331.4K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
#


class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False for x in range(len(s))] for y in range(2)]
        min_cut = [len(s)-x-1 for x in range(len(s)+1)]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i-1, -1):
                if s[i] == s[j]:
                    dp[i&1][j] = dp[(i+1)&1][j-1] if i+1 <= j-1 else True
                else:
                    dp[i&1][j] = False
                if dp[i&1][j]:
                    if min_cut[j+1] + 1 < min_cut[i]:
                        min_cut[i] = min_cut[j+1] + 1

        return min_cut[0]

