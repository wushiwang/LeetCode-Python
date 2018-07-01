#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (38.32%)
# Total Accepted:    42.9K
# Total Submissions: 112K
# Testcase Example:  '"eceba"\n2'
#
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
#
#
#
# For example,
#
# Given s = “eceba” and k = 2,
#
#
#
# T is "ece" which its length is 3.
#


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or k == 0:
            return 0
        dic, res = dict(), 0
        L = 0
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
                while len(dic) > k:
                    dic[s[L]] -= 1
                    if dic[s[L]] == 0:
                        dic.pop(s[L])
                    L += 1
            res = max(res, i-L+1)
        return res
