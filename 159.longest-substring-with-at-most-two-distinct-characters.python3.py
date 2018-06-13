#
# [159] Longest Substring with At Most Two Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Hard (43.18%)
# Total Accepted:    39.2K
# Total Submissions: 90.9K
# Testcase Example:  '"eceba"'
#
# Given a string s , find the length of the longest substring t  that contains
# at most 2 distinct characters.
#
# Example 1:
#
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
#
#
# Example 2:
#
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
#


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dic, res = dict(), 1
        L = R = 0
        while R < len(s):
            if s[R] in dic:
                dic[s[R]] += 1
                res = max(res, R-L+1)
            else:
                dic[s[R]] = 1
                while len(dic) == 3:
                    dic[s[L]] -= 1
                    if dic[s[L]] == 0:
                        dic.pop(s[L])
                    L += 1
                res = max(res, R-L+1)
            R += 1
        return res
